from database.dac import PostgressDac
from loguru import logger

import pandas as pd


def select_pasture_area_master():
    try:
        query = """
            SELECT idx, area 
            FROM pasture_area_master pam 
            WHERE useflag = 'Y'
        """
        return PostgressDac.execute_v2(query)['data']
        
    except Exception as e:
        logger.error(e)
        return None
    

def insert_pasture_master(data: pd.DataFrame):
    try:
        query = """
            INSERT INTO pasture_master
            (area, farm_nm, rprsntv, fond_de, farm_ar, brd_lvstck_co, prdctn_qy, farm_intrcn, addr, tlphon_no, hmpg, rdnmadr, nw_zip, la, lo)
            VALUES (%s)
        """
        
        param = data.copy()
        param = list(param.itertuples(index=False, name=None))
        
        return PostgressDac.executemany(query, param)['count']
    
    except Exception as e:
        logger.error(e)
        return False