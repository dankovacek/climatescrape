import os

import numpy as np
import pandas as pd
import math
import os
import sys
import time
import utm
import wget

from helper_functions import load_data

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data/')

print('dirname = ', DATA_DIR)

stn_df = load_data('Station_Inventory_EN.csv', DATA_DIR)

# input target location decimal degrees [lat, lon]
squamish_utm_loc = utm.from_latlon(50.336, -122.802161)
pemberton_utm_loc = utm.from_latlon(49.796, -123.203)

stn_df['distance_to_squamish'] = np.sqrt((stn_df['utm_E'] - squamish_utm_loc[0])**2 +
                                         (stn_df['utm_N'] - squamish_utm_loc[1])**2)


stn_df['distance_to_pemberton'] = np.sqrt((stn_df['utm_E'] - pemberton_utm_loc[0])**2 +
                                          (stn_df['utm_N'] - pemberton_utm_loc[1])**2)

# pull the station IDs for all stations within 10km of stations
pemberton_stns = stn_df[stn_df['distance_to_pemberton'] < 10000]
pemberton_stns.dropna(axis=0, how='any', subset=[
                      'MLY First Year', 'MLY Last Year'], inplace=True)
squamish_stns = stn_df[stn_df['distance_to_squamish'] < 10000]
squamish_stns.dropna(axis=0, how='any', subset=[
                     'MLY First Year', 'MLY Last Year'], inplace=True)
# print(pemberton_stns.head())

t_frame = 2  # 2 corresponds to daily, 1 to hourly, 3 to monthly
# for hourly, need to add '&Day={}' back in following '&month={}'
year = 1990
month = [e for e in range(1, 13)]
station_id = 1

for index, row in pemberton_stns.iterrows():
    years = [e for e in range(
        int(row['MLY First Year']), int(row['MLY Last Year']) + 1)]
    for year in years:
        ec_base_url = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?'
        ec_url = ec_base_url + 'format=csv&stationID={}&Year={}&Month={}&Day=14&timeframe={}&submit=Download+Data'.format(
            row['Station ID'], year, 1, t_frame)
        print(ec_url)
        filename = wget.download(ec_url)

        print(filename)
