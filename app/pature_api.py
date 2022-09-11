from cmath import log
from turtle import pos
from loguru import logger
from common import env
from database import postgress

import requests

API_URL = env.API_URL
API_API_KEY = env.API_API_KEY


def get_data(start_index: int, end_index: int, area: str):
    try:
        url = API_URL.replace('&API_API_KEY&', API_API_KEY).replace('&START_INDEX&', str(start_index)).replace('&END_INDEX&', str(end_index))
        payload = { 'AREA': area }
        
        req = requests.get(url=url, params=payload)
        return req.json()
        
    except Exception as e:
        logger.error(e)
        return {}
    

def run():
    try:
        process_count = 0
        data = postgress.select_pasture_area_master()
        
        print(data['data'])
        
        for row in data['data']:
            area = row[data['column'].index('area')]
            
            loop = True
            start_index = 1
            index_Increase = 9
            
            while(loop):
                end_index = start_index + index_Increase
                data = get_data(start_index, end_index, area)
                process_count += postgress.insert_pasture_master(data)
                
                start_index = end_index + 1
                if end_index > int(data[env.API_NAME]['totalCnt']):
                    loop = False
        
    except Exception as e:
        logger.error(e)
        return False