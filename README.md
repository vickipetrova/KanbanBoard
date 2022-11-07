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
flask init-db
pip install -e .
python3 app.py
```
# Testing

Go to the main folder KanbanBoard and run the following commands from there. 

First make sure to the environment is activated and the app is installed as a package:

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip install -e .
```

Then install the coverage and run the tests:
```bash
pip install pytest coverage
pytest
```

To measure the code coverage of the tests use the `coverage` command instead of running `pytest` directly. 
```bash
coverage run -m pytest
```

You can create a coverage report in the reminal:
```bash
coverage report
```

You can also create an HTML report where you can see which lines are covered in each of the files. It will create files in the `htmlcov` folder. To view  the report open `htmlcov/index.html` in a browser. 
```bash
coverage html
```