import os
from dotenv import load_dotenv

load_dotenv()


ENV = os.environ.get("ENV")
API_REQUEST_URL = os.environ.get("API_REQUEST_URL")

# mongodb
MONGODB_URL=os.environ.get("MONGODB_URL")
MONGODB_DB=os.environ.get("MONGODB_DB")
MONGODB_COLLECTION=os.environ.get("MONGODB_COLLECTION")