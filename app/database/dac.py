from pymongo import MongoClient
from common import env
from loguru import logger

import pandas.io.sql as psql
import psycopg2 as pg2


class MongoDac():
    client = MongoClient(env.MONGODB_URL)
    db = client[env.MONGODB_DB]
    collection = db[env.MONGODB_COLLECTION] 
    
    @staticmethod
    def insert_one(data: dict):
        return MongoDac.collection.insert_one(data).inserted_id
    
    @staticmethod
    def insert_many(data: dict):
        return MongoDac.collection.insert_many(data).inserted_ids
    
    
class PostgressDac():
    @classmethod
    def execute(cls, query: str):
        try:
            with pg2.connect(
                database = env.POSTGRESSDB_DATABASE,
                user = env.POSTGRESSDB_USER,
                password = env.POSTGRESSDB_PASSWORD,
                host = env.POSTGRESSDB_HOST,
                port = env.POSTGRESSDB_PORT
            ) as conn:
                with conn.cursor() as cur:
                    conn.autocommit = True  
                    cur.execute(query)
                    
                    return { 'result': True, 'count': cur.rowcount, 'data': cur.fetchall() } 
            
        except (Exception, pg2.DatabaseError)  as e:
            logger.error(e)
            return { 'result': False, 'count': 0,'data': None }
                
        
    @classmethod
    def execute_v2(cls, query: str):
        try:
            with pg2.connect(
                database = env.POSTGRESSDB_DATABASE,
                user = env.POSTGRESSDB_USER,
                password = env.POSTGRESSDB_PASSWORD,
                host = env.POSTGRESSDB_HOST,
                port = env.POSTGRESSDB_PORT
            ) as conn:
                conn.autocommit = True  
                return { 'result': True, 'data': psql.read_sql(query, conn) }
            
        except (Exception, pg2.DatabaseError)  as e:
            logger.error(e)
            return { 'result': False, 'data': None }
        
        
    @classmethod
    def execute_parm(cls, query: str, param):
        try:
            with pg2.connect(
                database = env.POSTGRESSDB_DATABASE,
                user = env.POSTGRESSDB_USER,
                password = env.POSTGRESSDB_PASSWORD,
                host = env.POSTGRESSDB_HOST,
                port = env.POSTGRESSDB_PORT
            ) as conn:
                with conn.cursor() as cur:
                    conn.autocommit = True  
                    cur.execute(query, param)
                    
                    return { 'result': False, 'count': cur.rowcount, 'data': cur.fetchall() } 
            
        except (Exception, pg2.DatabaseError)  as e:
            logger.error(e)
            return { 'result': False, 'count': 0,'data': None }
        
    
    @classmethod
    def executemany(cls, query: str, param: list):
        try:
            with pg2.connect(
                database = env.POSTGRESSDB_DATABASE,
                user = env.POSTGRESSDB_USER,
                password = env.POSTGRESSDB_PASSWORD,
                host = env.POSTGRESSDB_HOST,
                port = env.POSTGRESSDB_PORT
            ) as conn:
                with conn.cursor() as cur:
                    conn.autocommit = True  
                    cur.executemany(query, param)
                    
                    return { 'result': False, 'count': cur.rowcount, 'data': cur.fetchall() } 
            
        except (Exception, pg2.DatabaseError)  as e:
            logger.error(e)
            return { 'result': False, 'count': 0, 'data': None }
        
