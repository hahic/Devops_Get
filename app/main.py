from config import logger as cnf_logger
from common import env
from loguru import logger


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
    
    logger.info('*' * 10)