import unittest
import requests

class TestMainBoard(unittest.TestCase):
    """
    Test the main baord
    """

    def test_board_components(self):
        """
        Tests to make sure the board has all important main components.
        These include the title, the button to add a new task and all columns of the table. 
        """
        response = requests.get('http://localhost:8000/')
        self.assertTrue("Kanban Board" in response.text)
        self.assertTrue("Add Task" in response.text)

        columns = ["Name", "Status", "Description", "Remove"]
        for column in columns:
            self.assertTrue(column in response.text)

    def test_homepage(self):
        """
        Tests to make sure the Kanban loads the main page and does not redirect to any other pages. 
        """
        response = requests.get('http://localhost:8000/')
        self.assertEqual(response.url,'http://localhost:8000/')

    def test_add_task(self):
        """
        Tests whether adding a new task works. 

        Creates a task with unique name and checks whether the task was added to the table.

        Ideally this test would add a task, then get the data from the server, and check
        whetehr the number of tasks increased + whether the new task is in there.
        However, I could not retrieve the data from the table to do that so the test is simpler.
        """
        import uuid
        task_name = str(uuid.uuid4())
        url = 'http://localhost:8000/'
        new_task = {"button": "add_task", "task_name": task_name, "task_description": "TEST"}

        requests.post(url, new_task)

        response = requests.get('http://localhost:8000/')
        self.assertTrue(task_name in response.text)
        self.assertTrue("TEST" in response.text) 
        
    def test_change_status(self):
        """
        Tests whether the status of a task updates correctly. 

        I could not implement this test because of the reason mentioned above: I can't get the
        data of the tasks from the table.

        The test should:
        - add a new task
        - get its id
        - send post request to change its status from "To-do" to "In progress" and check it.
        - send post request to change its status from "In progress" to "Completed" and check it.
        """
        pass

    def test_delete_task(self):
        """
        Tests whether taska are deleted correctly.

        I could not implement this test because of the reason mentioned above: I can't get the
        data of the tasks from the table.

        The test should:
        - get the task id-s from the last 2 tasks (added in 2 previous tests)
        - delete the first one, check that tasks decreased by 1 and it's not there
        - repeat for the second task
        """
        pass


if __name__ == "__main__":
    unittest.main()