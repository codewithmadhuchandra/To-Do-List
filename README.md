# Flask Todo List Application

A simple and efficient Todo List application built with Flask and SQLAlchemy. This application allows users to manage their tasks with basic CRUD operations.

## Features

- Add new tasks
- Edit existing tasks
- Mark tasks as complete/incomplete
- Delete tasks
- Persistent storage using SQLite database

## Tech Stack

- Python
- Flask (Web Framework)
- SQLAlchemy (ORM)
- SQLite (Database)
- HTML/CSS (Frontend)

## Project Structure

```
.
├── app.py              # Main application file
├── instance/           # Database instance directory
└── templates/          # HTML templates
    ├── home.html       # Main todo list page
    └── edit.html       # Task editing page
```

## Setup and Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask flask-sqlalchemy
```

4. Run the application:
```bash
python app.py
```

5. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

- **Add Task**: Enter a task in the input field and click "Add"
- **Edit Task**: Click the edit button next to a task
- **Mark Complete**: Click the checkbox to toggle task completion
- **Delete Task**: Click the delete button to remove a task

## Database

The application uses SQLite as its database, which is automatically created in the `instance` directory when you first run the application. The database file is named `todo_app.db`.

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is open source and available under the [MIT License](LICENSE). 