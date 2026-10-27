# Task Tracker

A simple, menu-based Python command-line utility to track tasks. Tasks are saved persistently in a `tasks.json` file.

## Features
- **Add Tasks**: Enter a title to add a task with a default 'Pending' status.
- **View Tasks**: Lists all current tasks with their state ('Pending' or 'Done').
- **Complete Tasks**: Select a task by its index number and mark it as completed.
- **Delete Tasks**: Remove tasks from your list.
- **Persistent Storage**: Automatically saves and loads tasks using standard JSON.
- **Error Handling**: Friendly warnings for empty titles, invalid index selection, and formatting.

## How to Run
Execute the program in your terminal:
```bash
python mini_task_tracker.py
```
