import logging

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('logs/log_intg.log'),
        logging.StreamHandler(),
    ],
)

logger_load = logging.getLogger('load_data_sql_postgres')
