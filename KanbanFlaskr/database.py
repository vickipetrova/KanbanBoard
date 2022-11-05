import uuid

# Store the tasks as a list of dictionaries.
# No need for a Task class because we won't use any additional functionalities. 
tasks = [
    # Create static tasks (always pop up in the table). 
        # {
        #     'id':1, 
        #     'name':'Task1', 
        #     'description':'Description of Task1',
        #     'status': 'To-do'
        # },
        # {
        #     'id':2,
        #     'name':'Task2', 
        #     'description':'Description of Task2',
        #     'status':'In progress'
        # },
        # {
        #     'id':3,
        #     'name':'Task3', 
        #     'description':'Description of Task3',
        #     'status':'Completed'
        # }
]

def get_tasks(): 
    """
    A function to fetch the existing tasks.

    Parameters
    ----------
    None

    Output
    ------
    tasks: list of dicts
        Each dictionary represents a task with id, name, description, and status. 
    """
    return tasks 


def add_task(task_name, task_description):
    """
    A function to add a new task to the list of existing tasks. 

    Parameters
    ----------
    task_name: str
        The name of the task.
    task_description: str
        The description of the task.

    Output
    ------
    None
    """

    tasks.append({
        'id': uuid.uuid4(), # create a unique id
        'name': task_name,
        'description': task_description,
        'status': "To-do"
    })

def update_task_status(task_id):
    """
    A function to change the status of an existing task. 

    The change of status is incremental: 
    - "To-do" becomes "In progress"
    - "In progress" becomes "Completed"
    - "Completed" becomes "To-do"

    Parameters
    ----------
    task_id: UUID4
        The unique id of the task,

    Output
    ------
    None
    """

    # Find the task using the task id. 
    for task in tasks:

        if str(task['id']) == task_id:
            # Change the status accordingly. 
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
    """
    A function to delete an existing task. 

    Parameters
    ----------
    task_id: UUID
        The unique ID of the task to be deleted.

    Output
    ------
    None
    """
    # Find the task using the id and remove it from the list. 
    for i, task in enumerate(tasks):
        if str(task['id']) == task_id:
            tasks.pop(i)

