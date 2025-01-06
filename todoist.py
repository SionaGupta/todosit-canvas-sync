from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv
from datetime import datetime
import pytz
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

def convert_due_date(due_at):
     user_timezone = America/Los_Angeles

    # Parse the ISO 8601 date-time string into a datetime object
    parsed_datetime = datetime.fromisoformat(due_at)

    # Convert the datetime to the user's timezone
    target_timezone = pytz.timezone(user_timezone)
    localized_datetime = parsed_datetime.astimezone(target_timezone)

    # Format the date as "YYYY-MM-DD"
    formatted_date = localized_datetime.strftime("%Y-%m-%d")
    return formatted_date

def add_oneassignment(assignment, project_id):
    # wororkeokp
    try:
        duedate = convert_due_date(assignment.due_at)
        task = api.add_task(content=assignment.name, project_id=project.id, section_id=section_id, due=duedate)

    except Exception as error:
        print(error) 

