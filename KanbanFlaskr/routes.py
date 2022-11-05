from flask import render_template, request, redirect, url_for
from KanbanFlaskr import app
from KanbanFlaskr import database as db

# The main page with the Kanban board. 
@app.route('/')
def mainboard():
    return render_template("index.html", tasks = db.get_tasks())

@app.route('/', methods = ['POST'])
def mainboard_post():
    """
    Handle HTTP POST requests from the main page.

    There are 3 different types of POST requests on the main board:
    - Create a new task, coming from the "add_task" button.
    - Changing task status, coming from the "update_status" button.
    - Deleting a task, coming from the "delete_taks" button.

    Parameters
    ----------
        None

    Outputs
    -------
        None
    """
    # Handle POST requests differently according to the button the request came from.
    if request.form["button"] == "add_task":
        task_name = request.form.get('task_name')
        task_description = request.form.get('task_description')
        db.add_task(task_name, task_description)

    elif request.form["button"] == "update_status":
        task_id = request.form.get('task_id')
        db.update_task_status(task_id)

    elif request.form["button"] == "delete_task":
        task_id = request.form.get('task_id')
        db.delete_task(task_id)
    
    return redirect(url_for('mainboard'))

    # I did not use render template because, on refreshing the page the form is submitted every time.
    # This can be fixed with Java script but I have never used it before so I am leaving it
    # as an improvement for the future. 
    
    # return render_template("index.html", tasks = db.get_tasks())



