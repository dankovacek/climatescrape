import os

import numpy as np
import pandas as pd
import math
import os
import sys
import time
import utm

from helper_functions import load_data

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data/')

print('dirname = ', DATA_DIR)

stn_df = load_data('Station_Inventory_EN.csv', DATA_DIR)

# input target location decimal degrees [lat, lon]
pemberton_utm_loc = utm.from_latlon(50.336, -122.802161)
squamish_utm_loc = utm.from_latlon(49.796, -123.203)

stn_df['distance_to_squamish'] = np.sqrt((stn_df['utm_E'] - squamish_utm_loc[0])**2 +
                                         (stn_df['utm_N'] - squamish_utm_loc[1])**2)


stn_df['distance_to_pemberton'] = np.sqrt((stn_df['utm_E'] - pemberton_utm_loc[0])**2 +
                                          (stn_df['utm_N'] - pemberton_utm_loc[1])**2)

# enter the distance from the target to search for stations
search_radius = 10000

# pull the station IDs for all stations within 10km of stations
pemberton_stns = stn_df[stn_df['distance_to_pemberton'] < search_radius]
pemberton_stns = pemberton_stns.dropna(axis=0, how='any', subset=[
    'MLY First Year', 'MLY Last Year'])
squamish_stns = stn_df[stn_df['distance_to_squamish'] < search_radius]
squamish_stns = squamish_stns.dropna(axis=0, how='any', subset=[
    'MLY First Year', 'MLY Last Year'])

t_frame = 2  # 2 corresponds to daily, 1 to hourly, 3 to monthly
# for hourly, need to add '&Day={}' back in following '&month={}'

for index, row in squamish_stns.iterrows():
    rec_start = int(row['MLY First Year'])
    rec_end = int(row['MLY Last Year'])
    years = [e for e in range(rec_start, rec_end + 1)]
    frames = []
    all_data = pd.DataFrame()

    for year in years:
        ec_base_url = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?'
        ec_url = ec_base_url + 'format=csv&stationID={}&Year={}&Month={}&Day=14&timeframe={}&submit=Download+Data'.format(
            row['Station ID'], year, 1, t_frame)

        df = pd.read_csv(ec_url, header=23, parse_dates=['Date/Time'])

        frames += [df]

    all_data = pd.concat(frames)
    stn_name = str(stn_df[stn_df['Station ID'] ==
                          row['Station ID']].Name.item())
    new_file_name = os.path.join(DATA_DIR, stn_name + '_' +
                                 str(row['Station ID']).strip() + '_ID' +
                                 str(rec_start) + '_to_' + str(rec_end) + '.csv')
    all_data.to_csv(new_file_name)
