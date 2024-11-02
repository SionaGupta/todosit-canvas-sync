from todoist_api_python.api import TodoistAPI
from test import TODOIST_API

api = TodoistAPI(TODOIST_API)

try:
    projects = api.get_projects()
    print(projects[0].name)
    print(projects[1].name)
    print(projects[2].name)
    # print(projects)
except Exception as error:
    print(error)