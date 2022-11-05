from flask import render_template, request
from KanbanFlaskr import app
from KanbanFlaskr import database as db

# a simple page that says hello
@app.route('/')
def mainboard():
    return render_template("index.html", tasks = db.get_tasks())

@app.route('/', methods = ['POST'])
def mainboard_post():

    if request.form["button"] == "add_task":
        task_name = request.form.get('task_name')
        task_description = request.form.get('task_description')
        db.add_task(task_name, task_description)

    elif request.form["button"] == "update_status":
        task_id = int(request.form.get('task_id'))
        db.update_task_status(task_id)
    elif request.form["button"] == "delete_task":
        task_id = int(request.form.get('task_id'))
        db.delete_task(task_id)
    

    return render_template("index.html", tasks = db.get_tasks())




@app.route('/congrats')
def congrats():
    return "Congrats"

