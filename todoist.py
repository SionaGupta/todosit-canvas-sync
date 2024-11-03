from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into the environment

print(os.getenv("test_key"))
api = TodoistAPI(os.environ.get('TODOIST_API_KEY'))


try:
    projects = api.get_projects()

    for project in projects:
        print(project.name)
        try:
            task = api.add_task(content="Buy Milk", project_id=project.id)
            print(task)
        except Exception as error:
            print(error)

    # print(projects)
except Exception as error:
    print(error)