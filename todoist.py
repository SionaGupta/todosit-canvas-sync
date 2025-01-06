from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into the environment

print(os.getenv("test_key"))
api = TodoistAPI(os.environ.get('TODOIST_API_KEY'))

def add_assignments(assignments, course_name)
    
    # find project ID
    projects = api.get_projects()

    for project in projects: 
        if (project.name == "College Classes"):
            project_id = project.id

    try:
        sections = api.get_sections(project_id=project_id)
        print(sections)
    except Exception as error:
        print(error)

    # check if section exists 
    for section in sections: 
        if (course_name == section.name):
            section_id = section.id  
        else: 
            section = api.add_section(name=course_name, project_id=project_id)
            for section in sections: 
                if (course_name == section.name):
                    section_id = section.id  
    
    for assignment in assignments: 
        add_oneassignment(assignment, project_id, section_id)



def add_oneassignment(assignment, project_id):
    # wororkeokp
    try:
        # duedate = assignment.due
        task = api.add_task(content=assignment.name, project_id=project.id, section_id=section_id, due=duedate)

    except Exception as error:
        print(error) 
