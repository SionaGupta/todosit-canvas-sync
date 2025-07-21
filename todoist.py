from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv
from datetime import datetime
import pytz
import os

california_tz = pytz.timezone('America/Los_Angeles')


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

    sections = api.get_sections(project_id=project_id)

    # find section id
    for section in sections: 
        print (section.name + " " + course_name)
        if (course_name == section.name):
            print("right")
            section_id = section.id  
 
    for assignment in assignments: 
        add_oneassignment(assignment, project_id, section_id)
    
def time_pst(date):
    utc_dt = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    utc_dt = pytz.utc.localize(utc_dt)
    california_dt = utc_dt.astimezone(california_tz)
    california_dt = str(california_dt)
    print(california_dt)
    return california_dt


def add_oneassignment(assignment, project_id, section_id):
    # wororkeokp
    try:
        duedate = assignment['due_at']
        duedate = time_pst(duedate);
        date = duedate[:15]
        print(assignment['name'] + " " + duedate)

        sub = assignment['submission']
      
        print(sub['attempt'])
        print(sub['attempt']!= None)
        active = sub['attempt']!= None
        
        task_data = {
            'content': assignment['name'],  # Task content
            'project_id': project_id,       # Project ID
            'section_id': section_id,       # Section ID
            'due_date': date,  # Task due date
            'priority': 2,
            'is_completed': active
        }

        alltasks = api.get_tasks(project_id=project_id, section_id=section_id)

     
        
        #Check if current task is already listed
        for alltask in alltasks:
            if (assignment['name'] == alltask.content): 
                #if listed, check if completion is the same
                if not (active == alltask.is_completed):
                    task_id = alltask.id 
                    #update task if different
                    update = api.update_task(
                        task_id=task_id,
                        is_completed = active)
                    print(update)
            else: 
                #add task
                task = api.add_task(**task_data)
                print(task)
                
            
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
