from dataclasses import dataclass, field
from datetime import datetime
import os
from uuid import uuid4
import json
from pathlib import Path

import humanize

MAX_TITLE_LENGTH = 50
MAX_CONTENT_LENGTH = 1000
DEFAULT_DB_PATH = os.getenv("JOURNAL_DB_PATH", "journal.json")


@dataclass
class JournalEntry:
    title: str
    content: str
    tags: list[str] = field(default_factory=list)
    date: str = field(default_factory=lambda: datetime.now().isoformat())
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self):
        if not self.title.strip() or len(self.title) > MAX_TITLE_LENGTH:
            raise ValueError(
                f"Title must be non-empty and ≤ {MAX_TITLE_LENGTH} characters."
            )
        if not self.content.strip() or len(self.content) > MAX_CONTENT_LENGTH:
            raise ValueError(
                f"Content must be non-empty and ≤ {MAX_CONTENT_LENGTH} characters."
            )

    @property
    def relative_date(self) -> str:
        dt = datetime.fromisoformat(self.date)
        return humanize.naturaltime(datetime.now() - dt)


class JournalDatabase:
    def __init__(self, db_file: Path):
        self.db_file = db_file
        if isinstance(db_file, Path):
            self.db_file.touch(exist_ok=True)

    def load_entries(self) -> list[JournalEntry]:
        """Load entries from the journal database."""
        try:
            with open(self.db_file) as f:
                return [JournalEntry(**e) for e in json.load(f)]  # type: ignore
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_entries(self, entries: list[JournalEntry]) -> None:
        """Save journal entries to the database file."""
        with open(self.db_file, "w") as f:
            json.dump([e.__dict__ for e in entries], f, indent=2)

    def add_entry(self, title: str, content: str, tags: list[str]) -> None:
        entry = JournalEntry(title=title, content=content, tags=tags)
        entries = self.load_entries()
        entries.append(entry)
        self.save_entries(entries)

    def delete_entry(self, entry_id: str) -> None:
        entries = self.load_entries()
        entries = [e for e in entries if e.id != entry_id]
        self.save_entries(entries)

    @staticmethod
    def search_entries(
        entries: list[JournalEntry], query: str, titles_only: bool = False
    ) -> list[JournalEntry]:
        results = []
        for entry in entries:
            if titles_only:
                if query.lower() in entry.title.lower():
                    results.append(entry)
            else:
                if (
                    query.lower() in entry.title.lower()
                    or query.lower() in entry.content.lower()
                    or any(query.lower() in tag.lower() for tag in entry.tags)
                ):
                    results.append(entry)
        return results

    @staticmethod
    def filter_by_tag(entries: list[JournalEntry], tag: str) -> list[JournalEntry]:
        tag = tag.lower()
        return [e for e in entries if any(tag == t.lower() for t in e.tags)]
