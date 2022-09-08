import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.environ.get("ENV")
API_REQUEST_URL = os.environ.get("API_REQUEST_URL")