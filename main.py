from classes import information
from canvas import *
from todoist import *

term = "Summer 2025"

# gather all courses 
courses = list_current_courses(term)

for course in courses: 
    print(course['name'])


# loop over ever active course 
for course in courses:
    course_name = course['name']
    term = course['term']

    if (term['name'] == term):
        print(f"Course ID: {course['id']}, Name: {course['name']}")
        assignments = get_assignments(course['id'])
        add_assignments(assignments, course_name)   

