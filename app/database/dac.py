from pymongo import MongoClient
from common import env
from abc import *


class BaseDac(metaclass=ABCMeta):
    client = None
    db = None


class MongoDac(BaseDac):
    client = MongoClient(env.MONGODB_URL)
    db = client[env.MONGODB_DB]
    collection = db[env.MONGODB_COLLECTION] 
    
    @staticmethod
    def insert_one(data: dict):
        return MongoDac.collection.insert_one(data).inserted_id
    
    @staticmethod
    def insert_many(data: dict):
        return MongoDac.collection.insert_many(data).inserted_ids
    
    
# class PostgressDac(BaseDac):
#     client