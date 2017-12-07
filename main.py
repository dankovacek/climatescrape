import os

import numpy as np
import pandas as pd
import scipy.stats as sci_stats
import statsmodels.api as sm
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
squamish_utm_loc = utm.from_latlon(50.336, -122.802161)
pemberton_utm_loc = utm.from_latlon(49.796, -123.203)

stn_df['distance_to_squamish'] = np.sqrt((stn_df['utm_E'] - squamish_utm_loc[0])**2 +
                                         (stn_df['utm_N'] - squamish_utm_loc[1])**2)


stn_df['distance_to_pemberton'] = np.sqrt((stn_df['utm_E'] - pemberton_utm_loc[0])**2 +
                                          (stn_df['utm_N'] - pemberton_utm_loc[1])**2)

# pull the station IDs for all stations within 10km of stations
pemberton_stns = stn_df[stn_df['distance_to_pemberton'] < 10000]
squamish_stns = stn_df[stn_df['distance_to_squamish'] < 10000]

print(pemberton_stns.head(10))
