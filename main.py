import os
from pathlib import Path

from nicegui import ui

from backend import JournalDatabase

db_path = os.getenv("JOURNAL_DB_PATH", "journal.json")
db = JournalDatabase(Path(db_path))


@ui.refreshable
def journal_timeline():
    entries = db.load_entries()
    with ui.timeline(side="right"):
        for entry in entries:
            ui.timeline_entry(
                entry.content, title=entry.title, subtitle=entry.relative_date
            )


with ui.column().classes("w-full max-w-screen-xl mx-auto"):
    with ui.row().classes("w-full flex-nowrap gap-4"):
        with ui.column().classes("w-6/12"):
            journal_timeline()
        with ui.column().classes("w-6/12 pl-6"):
            with ui.card().classes("w-full max-w-md sticky top-4"):
                ui.label("Add New Entry").classes("text-lg font-bold")
                new_title = ui.input("Title").classes("w-full")
                new_content = ui.textarea("Content").classes("w-full")
                new_tags = ui.input("Tags (comma-separated)").classes("w-full")
                ui.button("Add Entry")


ui.run()
