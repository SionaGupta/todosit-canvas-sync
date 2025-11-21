import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into the environment

CANVAS_API_KEY  = os.environ.get('CANVAS_API_KEY')
BASE_URL = "https://ilearn.laccd.edu/api/v1"

requests = requests.Session()

# Set up headers for authentication
headers = {
    "Authorization": f"Bearer {CANVAS_API_KEY}"
}

def list_current_courses(term):
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
        #send only course for this term
        f_courses = [course for course in courses if course['term']['name'] == term]

        '''
        #print Current Courses 
        for course in f_courses: 
            print(course['name'])
            print("\n")
        '''
        
        return f_courses
    
    # Error        
    else:
            # error message
        error_message = f"Error {response.status_code}: {response.reason}"
        
        try:
            # additional details from the JSON error response
            error_details = response.json()
            error_message += f" - {error_details.get('errors', error_details.get('message', 'No additional details'))}"
        except ValueError: 
            # cases where the response isn't JSON
            pass
        print(error_message)


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
            # error message
        error_message = f"Error {response.status_code}: {response.reason}"
        
        try:
            #  additional details from the JSON error response
            error_details = response.json()
            error_message += f" - {error_details.get('errors', error_details.get('message', 'No additional details'))}"
        except ValueError:
            # not JSON
            pass
        print(error_message)

    return assignments 

