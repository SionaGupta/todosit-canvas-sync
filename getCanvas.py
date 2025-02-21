import requests
from dotenv import load_dotenv
from todoist import add_assignments 
import os

load_dotenv()  # Loads variables from .env into the environment

CANVAS_API_KEY  = os.environ.get('CANVAS_API_KEY')
BASE_URL = "https://ilearn.laccd.edu/api/v1"
curTerm = "Spring 2025"

def get_canvas_assignments(source):

    # start requests session
    requests = requests.Session()

    # Set up headers for authentication
    headers = {
        "Authorization": f"Bearer {source.API}"
    }