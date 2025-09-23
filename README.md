# TaskManager Python POO

## Educational Purpose

This project was created primarily for **educational and learning purposes**.
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Getting Started

1. Clone the repository
2. Join to the correct path of the clone
3. Execute: `python -m venv venv`
4. Execute in Windows: `venv\Scripts\activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Use `python -m src.models.TaskManager` -> everything in main of TaskManager.py will be executed.

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

Task manager developed in Python that allows you to manage personal or team activities. With this tool, users can create, edit and organize their tasks, assigning due dates and setting priorities. Ideal for those who need a simple but functional solution to organize their tasks effectively.

IMPORTANT: This project was created for practice POO

## Technologies used

1. Python

## Libraries used

#### Requirements.txt

```
pre-commit==4.3.0
```

#### Requirements.test.txt

```
pytest==8.4.2
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/TaskManager-Python-POO`](https://www.diegolibonati.com.ar/#/project/TaskManager-Python-POO)

## Testing

1. Join to the correct path of the clone
2. Execute in Windows: `venv\Scripts\activate`
3. Execute: `pytest --log-cli-level=INFO`

## Known Issues
