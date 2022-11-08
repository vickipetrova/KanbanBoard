# KanbanBoard 
A Kanban Board web app utilizing Flask, Python, HTML, CSS, and SQL, which I created for my Software Engineering CS162 class at Minerva University. 

## Functionalities

The users can:
1. Create new tasks
2. Change their state
3. Delete existing tasks

There are 3 categories for the states: to-do, in progress, and complete. 

### Key functionalities of the app include:
- User authentication

Users have a unique username and a password. I also restricted the length for the username strictly for the purposes of fitting it nicely in the table rather than having extremely long names. There are no additional requirements for the password. 
- Personalized Kanban board

In the main view users can see all tasks in the database created by anyone. However, in that case they will not be able to edit the tasks. If a users registers and logs into their account, then they will have all of features available to them. They will be able to create new tasks, only see the tasks they created in the personalized board and be able to edit them.  
- Edit existing tasks

Users are able to change the name, description, and status of a task. 
- SQL database for the tasks and users

A lot of the code is from or adapted from the Flask tutorial that we followed in class. 

## Future Extensions and Improvements

There are some aspects that can be improved and additional features that can be added. 

- Hash passwords to store them securely.
- Have additional requirements for the passwords (e.g. special characters, lowercase, uppercase, numbers).
- Having a bigger variety for the possible states of the tasks.
- Filtering of the tasks according to time, author, status. 
- Being able to assign tasks to other users.  
- Creating more tests for the main board view (current ones cover 75% of the code).


# Running the app

## MacOS

Use the following commands to initialize the databse and run the app. You can copy-paste all commands at once in the terminal:

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
# LO and HC tags

\#nudge: I used choice architecture in the design of the board with the tasks in order to guide the behaviour of the user in an ethical way. A user would be prompted to complete tasks since the color of a task with complete statuse is a more positive association compared with the red color of a task in to-do state. It does not guarantee to make users complete more tasks but would motivate them to do so to an extent. Other relevant choice architecture is when the user is not logged in, they see a big red X sign, which means they are not able to edit any tasks. To solve that they need to register and log in, which will allow them to make tasks and edit them. 

\#heuristics: I used the creative heuristic, called using an idea stimulating checklist, to debug my code. In the heursitic you go through a list of questions to answer why your problem is occuring. This is exactly the method I followed for debugginf problems. For example, I was getting an error that the create form sent 4 values but there were 3 columns. I listed the possbile causes: does the sql table define all neccessary properties of a task, is the table intitiated properly, when the table of users and posts are joined do I get all columns, is the HTML form correctly initialized. After going though this list of questions I was able to figure out that the task_status property was not selected in the JOIN statement and subsequently I could not use it. 

\#testability: This is a short HC tag but it is connected to the unit testing. With the help of the pytest library I was able to create numerous tests that test almost 100% of all the code to check that it is working in the expected way, including authentication, login, creating tasks, etc. Each test tests a hypothesis. For example, when adding a new task we expect to see it on the board, which is what the test does.

## LOs

\#testing - the code has extensive tests using the `pytest` library. The code passes all of them. The tests are well-designed and test crucial parts of the code. They als helped me while debugging. 

\#communication - The code has comments but they are not extensive since most of it was following the Flask tutorial resource from class. Still, there are comments at important lines of code. All of the code can be found on github where I wrote descriptive commit statements. The readme also provides a lot of useful information from features, to possible improvements, and instruction on how to run the app and tests. 

\#webstandards - I used many of the good standards when building a Flask app, including base template that is extended, blueprints, and url routing. The app combines Python, HTML, CSS, and SQLite effectively to solve the given task. A possible improvement is to also incorporate Javascript. It is the usual language used to handle functions instead of making the HTML more complicated. However, I have no prior experience so this is a future extension I can work on. 

\#separationofconcerns - All code is well designed and organized in a way that utilizes all technologies effectively. I also utilized the Singleton design pattern. Its benefits are that it can create a global point of contact for all clients though it can make unit testing harder. This example is connected to the database. Since connections are expensive to create or terminate, the app maintains one which can be used by all clients as it is accessible throughout program.