# 📝 Todo Task Manager

A simple yet powerful Python-based task management system that helps you organize, track, and manage your daily tasks efficiently.

---

## ✨ Features

- ✅ **Create Tasks** - Add new tasks with title and completion deadline
- 📋 **View Tasks** - Load and display all your tasks
- ✏️ **Update Status** - Mark tasks as completed
- 🗑️ **Delete Tasks** - Remove tasks by ID
- 💾 **Persistent Storage** - All tasks are saved to a JSON file
- 🔐 **Status Validation** - Tasks can only have valid statuses (PENDING, COMPLETED)
- ⏰ **Timestamps** - Automatic creation date tracking

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- No external dependencies required

### Installation
```bash
# Clone or download the repository
cd python-learn

# Run the application
python week1-todos.py
```

---

## 📖 Usage

### Creating a Task
```python
from week1_todos import todoTasks

# Initialize the todo manager
todo = todoTasks()

# Add a new task
todo.addTask("Buy groceries", "2026-04-20")
```

**Output:**
```json
{
  "id": 1,
  "taskTitle": "Buy groceries",
  "taskStatus": "PENDING",
  "createdAt": "2026-04-15",
  "completeBy": "2026-04-20"
}
```

### Deleting a Task
```python
# Delete task with ID 2
todo.delById(2)
```

### Updating Task Status
```python
# Mark task with ID 5 as completed
todo.updateStatus(5)
```

### Viewing All Tasks
```python
# Load and display all tasks
all_tasks = todo.tasks
for task in all_tasks:
    print(task)
```

---

## 📁 Project Structure

```
python-learn/
├── week1-todos.py      # Main application file
├── tasks.json          # Task data storage (auto-created)
└── README.md          # This file
```

---

## 🔧 API Reference

### `todoTasks` Class

#### `__init__()`
Initializes the todo manager and loads existing tasks from `tasks.json`.

#### `addTask(taskTitle: str, completeBy: str) -> str`
Creates a new task and returns JSON representation.
- **Parameters:**
  - `taskTitle`: Title/description of the task
  - `completeBy`: Deadline date (format: YYYY-MM-DD)
- **Returns:** JSON string of the created task

#### `delById(delId: int) -> None`
Deletes a task by its ID.
- **Parameters:**
  - `delId`: ID of the task to delete

#### `updateStatus(taskId: int) -> None`
Updates a task status to "Completed".
- **Parameters:**
  - `taskId`: ID of the task to update

#### `getNextId() -> int`
Returns the next available task ID (internal use).

#### `loadFile() -> list`
Loads tasks from `tasks.json` (internal use).

#### `writeToFile(tasks: list) -> None`
Persists tasks to `tasks.json` (internal use).

---

## 📊 Task Data Structure

Each task is stored as a JSON object:

```json
{
  "id": 1,
  "taskTitle": "Buy groceries",
  "taskStatus": "PENDING",
  "createdAt": "2026-04-15",
  "completeBy": "2026-04-20"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer | Unique task identifier |
| `taskTitle` | String | Task description |
| `taskStatus` | String | Current status (PENDING or COMPLETED) |
| `createdAt` | String | Task creation date (YYYY-MM-DD) |
| `completeBy` | String | Task deadline (YYYY-MM-DD) |

---

## 🐛 Known Issues & Tips

### Issue: `TypeError: 'frozenset' object is not subscriptable`
**Solution:** Don't try to index the `TASK_STATUSES` frozenset. Use string values directly:
```python
# ❌ Wrong
task['taskStatus'] = TASK_STATUSES[0]

# ✅ Correct
task['taskStatus'] = "PENDING"
```

---

## 💡 Future Enhancements

- [ ] Add task priority levels
- [ ] Implement task categories/tags
- [ ] Add due date reminders
- [ ] Create a CLI interface with menus
- [ ] Add task search functionality
- [ ] Export tasks to CSV/PDF
- [ ] Add data validation
- [ ] Create unit tests

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

Created as a learning exercise for Python fundamentals.

---

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements!

---

## 📞 Support

If you encounter any issues or have questions, please open an issue in the repository.

---

**Happy Task Managing! 🎉**
