import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.environ.get("ENV")

# api
API_NAME=os.environ.get("API_NAME")
API_URL=os.environ.get("API_URL")
API_API_KEY=os.environ.get("API_API_KEY")

# mongodb
MONGODB_URL=os.environ.get("MONGODB_URL")
MONGODB_DB=os.environ.get("MONGODB_DB")
MONGODB_COLLECTION=os.environ.get("MONGODB_COLLECTION")

# postgressdb
POSTGRESSDB_DATABASE=os.environ.get("POSTGRESSDB_DATABASE")
POSTGRESSDB_USER=os.environ.get("POSTGRESSDB_USER")
POSTGRESSDB_PASSWORD=os.environ.get("POSTGRESSDB_PASSWORD")
POSTGRESSDB_HOST=os.environ.get("POSTGRESSDB_HOST")
POSTGRESSDB_PORT=os.environ.get("POSTGRESSDB_PORT")