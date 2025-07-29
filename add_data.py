import os
from pathlib import Path

from backend import JournalDatabase

db_path = Path(os.getenv("JOURNAL_DB_PATH", "journal.json"))
if db_path.exists():
    db_path.unlink()

db = JournalDatabase(db_path)

entries = [
    (
        "Learned about dataclasses",
        "Explored the power of Python's dataclasses today.",
        ["python", "dataclass"],
    ),
    (
        "Built a journaling app",
        "Started a new journaling app using NiceGUI. Feels smooth!",
        ["project", "gui"],
    ),
    (
        "Deep dive into UUIDs",
        "Used uuid4 to uniquely identify journal entries.",
        ["uuid", "python"],
    ),
    (
        "Debugging JSON issues",
        "Ran into a JSONDecodeError—handled it gracefully.",
        ["debugging", "json"],
    ),
    (
        "Refactored old code",
        "Improved readability and reduced duplication in several modules.",
        ["refactoring", "clean-code"],
    ),
    (
        "Search by tags added",
        "Implemented tag filtering to narrow down results.",
        ["search", "tags"],
    ),
    (
        "Markdown rendering live",
        "Entries now support Markdown formatting in the UI.",
        ["markdown", "frontend"],
    ),
    (
        "Weekend CLI project",
        "Planning to build a command-line habit tracker.",
        ["cli", "ideas", "project"],
    ),
    (
        "Wrote some tests",
        "Added unit tests to ensure the journal DB behaves correctly.",
        ["testing", "quality"],
    ),
    (
        "Experimented with tailwind",
        "Started playing with Tailwind CSS for styling.",
        ["css", "frontend", "tailwind"],
    ),
]

for title, content, tags in entries:
    db.add_entry(title, content, tags)

print("✅ Seeded journal with 10 sample entries.")
