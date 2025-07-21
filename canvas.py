import requests
from dotenv import load_dotenv
from todoist import add_assignments 
from datetime import datetime
import os

load_dotenv()  # Loads variables from .env into the environment

CANVAS_API_KEY  = os.environ.get('CANVAS_API_KEY')
BASE_URL = "https://ilearn.laccd.edu/api/v1"
curTerm = "Summer 2025"


requests = requests.Session()

# Set up headers for authentication
headers = {
    "Authorization": f"Bearer {CANVAS_API_KEY}"
}

def get_assignments(course_id):
    # link
    url = f"{BASE_URL}/courses/{course_id}/assignments?per_page=100"

    # filter for active courses 
    params = {
        "include": "submission"  # Include the course term in the response
    }

    response = requests.get(url, headers=headers, params=params)

    assignments = []

    if response.status_code == 200:
        # convert from json
        assignments = response.json()
  
    # Error        
    else:
            # Simplify the error message
        error_message = f"Error {response.status_code}: {response.reason}"
        
        try:
            # Try to extract additional details from the JSON error response
            error_details = response.json()
            error_message += f" - {error_details.get('errors', error_details.get('message', 'No additional details'))}"
        except ValueError:
            # Handle cases where the response isn't JSON
            pass
        print(error_message)

    return assignments 


def list_current_courses():
    # link
    url = f"{BASE_URL}/courses"
    
    # filter for ac tive courses 
    params = {
        "enrollment_state": "active",  # Fetch only active courses
        "include": "term"  # Include the course term in the response

    }

    # collect data 
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        # convert from json
        courses = response.json()
        

        # loop over ever active course 
        for course in courses:
            course_name = course['name']
            term = course['term']

            if (term['name'] == curTerm):
                print(f"Course ID: {course['id']}, Name: {course['name']}")
                assignments = get_assignments(course['id'])
                add_assignments(assignments, course_name)
        

    # Error        
    else:
            # Simplify the error message
        error_message = f"Error {response.status_code}: {response.reason}"
        
        try:
            # Try to extract additional details from the JSON error response
            error_details = response.json()
            error_message += f" - {error_details.get('errors', error_details.get('message', 'No additional details'))}"
        except ValueError: 
            # Handle cases where the response isn't JSON
            pass
        print(error_message)





list_current_courses()