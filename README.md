# NiceGUI demo

A small front-end GUI to a dev journal (json) back-end.

## Setup

```
git clone git@github.com:bbelderbos/nicegui_demo.git
cd nicegui_demo
# install dependencies
uv sync
# add some fake data
uv run add_data.py
uv run main.py
# opens browser tab to go to http://localhost:8080
```

## Looks

Here we see a nice-looking NiceGUI front-end showing the 10 fake data entries we just generated. We can add + delete journal entries, after each operation the timeline automatically refreshes (thanks to the NiceGUI `@ui.refreshable` decorator).:

<img width="1798" height="1291" alt="Screenshot 2025-08-01 at 17 31 57" src="https://github.com/user-attachments/assets/ffe870b8-a40d-42d0-9f0a-246fa33f7171" />
