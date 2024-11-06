import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into the environment

CANVAS_API_KEY  = os.environ.get('CANVAS_API_KEY')


s = requests.Session()
s.headers.update({'Authorization': 'Bearer {CANVAS_API_KEY}'})

try:
    r = s.get('https://<canvas>/api/v1/courses')
except requests.exceptions.RequestException as e:  # This is the correct syntax
    raise SystemExit(e)