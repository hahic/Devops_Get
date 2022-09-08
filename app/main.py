from config import logger as cnf_logger
from common import env
from loguru import logger

if env.ENV == "dev":
    config = cnf_logger.DevelopConfig()
elif env.ENV == "production":
    config = cnf_logger.ProductionConfig()
    
logger.configure(**config.LOGURU_SETTINGS)