from canvas import *
from todoist2 import *


term = "Spring 2026"

print("\n")

# gather all courses 
courses = list_current_courses(term)


# loop over ever active course 
for course in courses:

    print(course['name'] + "\n")

    assignments = get_assignments(course['id'])


    info = add_section(course['name'])

    for assignment in assignments: 
        if assignment['due_at']:
            add_oneassignment(assignment, info['project'], info['section'])
            print('')
 


# Ending Todoist Task Signal
finish(info['project'])
