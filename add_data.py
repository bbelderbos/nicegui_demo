import os
from pathlib import Path

from backend import JournalDatabase

db_path = os.getenv("JOURNAL_DB_PATH", "journal.json")
db = JournalDatabase(Path(db_path))

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
]

for title, content, tags in entries:
    db.add_entry(title, content, tags)

print("Seeded journal with sample entries.")
