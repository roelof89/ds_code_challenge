# run script for 2-initial_data_transformation
import sys
import geopandas as gpd
import helper.functions as hf
from datetime import datetime

# make logger
logger = hf.make_logger('2-initial_data_transformation_run')

# functions
def threshold(data,col):
    fails = hf.count_na(data,col)
    df_set = data.shape[0]
    per = round(fails/df_set,2)
    if df_set > 500000 and per < .5:
        logger.info("Data passes the threshold of 0.5 and set greater than 500k")
        return True
    else:
        logger.error("Data failed the threshold of 0.5 and set greater than 500k")
        sys.exit()

def main():
    start = datetime.now()
    # read service data
    logger.info('Loading files')
    load_time = datetime.now()
    sr = hf.load_service_data('data/raw/sr.csv.gz')
    # read geojson
    geo = gpd.read_file('data/raw/city-hex-polygons-8.geojson')
    load_time = datetime.now() - load_time
    logger.info(f'Files loaded: {load_time}')

    # join using geospatial join
    logger.info("Joining files on geometry")
    join_time = datetime.now()
    sr.crs = geo.crs
    sr['h3_level8_index'] = sr.sjoin(geo, how='left')['index'] # only want the index col
    join_time = datetime.now() - join_time

    # apply threshold
    if threshold(sr, 'h3_level8_index'):
        logger.info(f"Finished join: {join_time}")
        sr = sr.drop(['geometry'], axis=1) # don't need to keep geometry data so dropping

        fails = hf.count_na(sr,'h3_level8_index')
        df_set = sr.shape[0]
        logger.info(f"Records failed join: {fails}")
        logger.info(f"Records total: {df_set}")
        logger.info(f"Join error: {round(fails/df_set, 2)*100}%")

        # make na hexs 0
        # If the data didn't join we have null so easier to populate the nulls and not deal with NA lat lons
        sr['h3_level8_index'] = sr['h3_level8_index'].fillna('0')

        sr.to_csv('data/trans/sr_hex.csv',index=None)
        end = datetime.now() - start
        logger.info(f"Done: Process took {end}")

if __name__ == '__main__':
    main()