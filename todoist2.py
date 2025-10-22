from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv
from datetime import datetime, date 
import pytz
import os

california_tz = pytz.timezone('America/Los_Angeles')
projectName = "Education 📚"

load_dotenv()  # Loads variables from .env into the environment

api = TodoistAPI(os.environ.get('TODOIST_API_KEY'))

# Get the section id
project_id = 1

# find project ID
projects = api.get_projects()
    
for project in projects: 
    if (project.name == projectName):
        project_id = project.id
        


def add_section(course_name):
    
    section_id = 1

    # Fetch Sections 
    try:
        sections = api.get_sections(project_id=project_id)
    except Exception as error:
        print(error)

    # If course section doesn't exist, create new section
    if not any(course_name == section.name for section in sections) or not sections:
        try:
            course_name = str(course_name)
            section = api.add_section(name=course_name, project_id=project_id)
        except Exception as error:
            print(error)
        print("Adding Section")

    # Refresh Sections
    sections = api.get_sections(project_id=project_id)

    # Find Section ID
    for section in sections: 
        if (course_name == section.name):
            print("Found Section " + section.name + "\n")
            section_id = section.id  
    
    info = {
    'project': project_id,
    'section': section_id
    }

    return info


def time_pst(date):
    utc_dt = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    utc_dt = pytz.utc.localize(utc_dt)
    california_dt = utc_dt.astimezone(california_tz)
    california_dt = str(california_dt)
    date = california_dt[:10]
    return date
    

def add_oneassignment(assignment, project_id, section_id):
    # wororkeokp
    try:
        taskdate = time_pst(assignment['due_at'])
        task_date_object = datetime.strptime(taskdate, "%Y-%m-%d").date()
        overdue = task_date_object < date.today()

        name = assignment['name']
        name = name.strip()

        print(name + " " + taskdate)
       
        active = assignment['submission']['attempt'] == None

        task_data = {
            'content': name,  # Task content
            'project_id': str(project_id),       # Project ID
            'section_id': str(section_id),       # Section ID
            'due_date': taskdate,  # Task due date
            'priority': 2,
        }

        alltasks = api.get_tasks(project_id=project_id, section_id=section_id)

        # Check if current task is already listed
        if alltasks:
            for alltask in alltasks:
                # if task is already there
                if (name == alltask.content):        
                    print('Active')

                    # if listed, check if task is completed since last update     
                    if (active == False):
                        task_id = alltask.id 
                        # update task if different
                        update = api.close_task(task_id=task_id)
                        print('Updated Completion ' + str(update))
                    
                    
                    # if listed, check if task is overdue   
                    if (overdue == True):
                        task_id = alltask.id 
                        update = api.close_task(task_id=task_id)
                        print('Overdue Task Removed ' + str(update))
                    
                    print("\n")

                    return 0;  

        print('Completed')

        # add task
        if (active == True and overdue == False):  
            task = api.add_task(**task_data)                
            print("Added " + task.name)

        print("\n")

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


def test_tasks(): 
    projects = api.get_projects()

    for project in projects: 
        if (project.name == projectName):
            sections = api.get_sections()
            for section in sections: 
                if (section.name == 'MATH 270 : Linear Algebra - Zheng A. - SUMMER 2025 - SECTION# 10425'):
                    try:
                        task = api.add_task(content="hello World", project_id=project.id, section_id=section.id)
                        print(task)
                    except Exception as error: 
                        print(error)


def finish(projectid):
    task = api.add_task(content="Updated Todoist!", project_id=projectid)
    print("Finished")