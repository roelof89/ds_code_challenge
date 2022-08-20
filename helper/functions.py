import os
import logging
import pandas as pd
import geopandas as gpd

def count_na(data,col):
    return data[data[col].isna()].shape[0]

def make_logger(file_name):
    LOG_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
    LOG_NAME = file_name
    LOG_FILE_INFO = os.path.join('log',f'{file_name}.log')
    LOG_FILE_ERROR = os.path.join('log',f'{file_name}.err')

    logger = logging.getLogger(LOG_NAME)
    log_formatter = logging.Formatter(LOG_FORMAT)

    # comment this to suppress console output
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    logger.addHandler(stream_handler)

    file_handler_info = logging.FileHandler(LOG_FILE_INFO, mode='w')
    file_handler_info.setFormatter(log_formatter)
    file_handler_info.setLevel(logging.INFO)
    logger.addHandler(file_handler_info)

    file_handler_error = logging.FileHandler(LOG_FILE_ERROR, mode='w')
    file_handler_error.setFormatter(log_formatter)
    file_handler_error.setLevel(logging.ERROR)
    logger.addHandler(file_handler_error)

    logger.setLevel(logging.INFO)
    return logger

def load_service_data(file_path):
    col_types = {
    'notification_number':str,
    'reference_number':str
    }
    date_cols = ['creation_timestamp','completion_timestamp']
    sr = pd.read_csv(file_path, compression='gzip', index_col=0, parse_dates=date_cols,dtype=col_types)
    sr = gpd.GeoDataFrame(sr, geometry=gpd.points_from_xy(sr.longitude, sr.latitude))
    return sr