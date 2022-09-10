from config import logger as cnf_logger
from common import env
from loguru import logger

import pature_api 


def setting_congfig():
    if env.ENV == "dev":
        config = cnf_logger.DevelopConfig()
    elif env.ENV == "production":
        config = cnf_logger.ProductionConfig()
        
    logger.configure(
        handlers=config.LOGURU_SETTINGS['handler'],
        levels=config.LOGURU_SETTINGS['levels']
    )


if __name__ == '__main__':
    setting_congfig()
    
    logger.info('*' * 62)
    logger.info(('*' * 20) + ' [program] devops_get ' + ('*' * 20))
    
    pature_api.run()
    
    logger.info('*' * 62)