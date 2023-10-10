from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.environ.get('MONGODB_URL'))

db = client.task_db

collection_name = db["task_collection"]
