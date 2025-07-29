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
            with ui.timeline_entry(
                entry.content, title=entry.title, subtitle=entry.relative_date
            ):
                with ui.row().classes("gap-2 flex-wrap"):
                    for tag in entry.tags:
                        if tag.strip():
                            ui.badge(tag)
                ui.button(
                    icon="delete",
                    on_click=lambda entry_id=entry.id: handle_delete_entry(entry_id),
                ).props("flat round dense color=red")


def handle_add_entry(title_input, content_input, tags_input):
    raw_tags = tags_input.value.split(",")
    tags = [tag.strip() for tag in raw_tags if tag.strip()]
    db.add_entry(title=title_input.value, content=content_input.value, tags=tags)
    ui.notify("Entry added", type="positive")
    journal_timeline.refresh()
    title_input.set_value("")
    content_input.set_value("")
    tags_input.set_value("")


def handle_delete_entry(entry_id: str):
    db.delete_entry(entry_id)
    ui.notify("Entry deleted", type="negative")
    journal_timeline.refresh()


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
                ui.button(
                    "Add Entry",
                    on_click=lambda: handle_add_entry(new_title, new_content, new_tags),
                )


ui.run()
