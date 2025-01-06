from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv
from datetime import datetime
import pytz
import os

load_dotenv()  # Loads variables from .env into the environment

print(os.getenv("test_key"))
api = TodoistAPI(os.environ.get('TODOIST_API_KEY'))

def add_assignments(assignments, course_name):
    
    section_id = 1
    project_id = 1
    # find project ID
    projects = api.get_projects()

    for project in projects: 
        if (project.name == "College Classes"):
            project_id = project.id
        

    try:
        sections = api.get_sections(project_id=project_id)
    except Exception as error:
        print(error)

    # check if section exists 
    # Check if the course name is not in any section's name
    if not any(course_name == section.name for section in sections) or not sections:
        try:
            course_name = str(course_name)
            section = api.add_section(name=course_name, project_id=project_id)
            print(section)
        except Exception as error:
            print(error)
        print("Adding Section")

    
    # find section id
    for section in sections: 
        if (course_name == section.name):
            section_id = section.id  
 
    for assignment in assignments: 
        add_oneassignment(assignment, project_id, section_id)


def add_oneassignment(assignment, project_id, section_id):
    # wororkeokp
    try:
        duedate = assignment['due_at']
        duedate = duedate[:10]

        task_data = {
            'content': assignment['name'],  # Task content
            'project_id': project_id,       # Project ID
            'section_id': section_id,       # Section ID
            'due_date': duedate,  # Task due date
            'priority': 2

        }

        alltasks = api.get_tasks(project_id=project_id, section_id=section_id)

        if not any(assignment['name'] == alltask.content for alltask in alltasks):
            task = api.add_task(**task_data)

    except Exception as error:
        print(error) 

def test_sections():

    projects = api.get_projects()

    for project in projects:
        try:
            section = api.add_section(name="Groceries", project_id=project.id)
            print(section)
        except Exception as error:
            print(error)

