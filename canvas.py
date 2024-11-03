import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into the environment

CANVAS_API_KEY  = os.environ.get('CANVAS_API_KEY')
params = {'appid': CANVAS_API_KEY} 

r = requests.get('https://<canvas>/api/v1/users/self/courses', params=params)