# KanbanBoard 
A Kanban Board web app utilizing Flask, Python, HTML, CSS, created for my Software Engineering CS162 class at Minerva University. 

## Functionalities

The users can:
1. Create new tasks
2. Change their state
3. Delete existing tasks

There are 3 categories for the states: to-do, in progress, done. 

The current app is very simple and has no extended functionalities. Improvements can include:
- Personalized Kanban board
- Editing existing tasks
- Improving the design
- Creating mroe extensive tests
- User authentication
- SQL database for the task and users

# Running the app

## MacOS
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```
# Testing

After the environment is activated, run the following commands in the terminal

```bash
pip install pytest coverage
pytest
pytest -v (verbose)
coverage run -m pytest
```
