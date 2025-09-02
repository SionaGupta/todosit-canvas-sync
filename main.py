from canvas import *
from todoist import *

term = "Fall 2025"

print("\n")

# gather all courses 
courses = list_current_courses(term)


# loop over ever active course 
for course in courses:

    print(course['name'])

    assignments = get_assignments(course['id'])

    info = add_section(course['name'])

    for assignment in assignments: 
        add_oneassignment(assignment, info['project'], info['section'])

    print("\n")  

finish(info['project'])

print("\n")