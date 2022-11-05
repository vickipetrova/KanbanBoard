import random
def get_name():
    return random.choice(["Helen", "Vicki"])

tasks = [
        {
            'id':1, 
            'name':'Task1', 
            'description':'Description of Task1',
            'status': 'To-do'
        },
        {
            'id':2,
            'name':'Task2', 
            'description':'Description of Task2',
            'status':'In progress'
        },
        {
            'id':3,
            'name':'Task3', 
            'description':'Description of Task3',
            'status':'Completed'
        }
]

def get_tasks(): return tasks 


def add_task(task_name, task_description):

    tasks.append({
        'id': len(tasks) + 1,
        'name': task_name,
        'description': task_description,
        'status': "To-do"
    })

def update_task_status(task_id):
    for task in tasks:
        if task['id'] == task_id:
            if task['status'] == "To-do":
                task['status']  = "In progress"
            elif task['status'] == "In progress":
                task['status']  = "Completed"
            elif task['status'] == "Completed":
                task['status']  = "To-do"
            else:
                print("Error: task status is wrong. ")
            break
        
def delete_task(task_id):
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks.pop(i)

