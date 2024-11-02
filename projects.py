from todoist_api_python.api import TodoistAPI
try:
    import dotenv
    print("python-dotenv is installed successfully!")
except ImportError:
    print("python-dotenv is not installed.")
import os

load_dotenv()  # Loads variables from .env into the environment

TODOSIT_API_KEY = os.getenv("TODOSIT_API_KEY")


api = TodoistAPI(TODOSIT_API_KEY)

try:
    projects = api.get_projects()

    for project in projects:
        print(project.name)

    # print(projects)
except Exception as error:
    print(error)