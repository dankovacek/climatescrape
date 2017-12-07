# EC Climate Data Scraper

A python script for pulling climate data from archived data from
Environment Canada (http://climate.weather.gc.ca).  

### Environment, Dependencies
Python 3.[4, 5, 6].  Python 3.5 is only version verified.

For packages, see requirements.txt.  The only unusual package is utm,
but it can be worked around without too much trouble.  

### Setup
  1.  Clone repo to local system.
  2.  `>>virtualenv -p python3 env`
  3.  If virtualenv not activated: `>>source env/bin/activate` (from main folder)
  4.  `>>pip install requirements.txt`
  5.  `>>python main.py`
  6.  Get coordinates for location(s) (in Canada) you want to check for the nearest
      stations.
  7.  Enter the coordinates in lat/lon (or just as a tuple in UTM northing/easting):

  ```
  # input target location decimal degrees [lat, lon]
  squamish_utm_loc = utm.from_latlon(50.336, -122.802161)
  pemberton_utm_loc = utm.from_latlon(49.796, -123.203)
  ```

  8.  Set a search radius (in m) to bound your search from the target location:
  `search_radius = 10000`
  9.  Set a timeframe (1 = hourly, 2 = daily, 3 = monthly), e.g.:  
  `t_frame = 2`  

### Execution

The example code has a default random lat/lon location near Squamish, BC.

Once you have addressed all of the input parameters in `Setup`:
  * `>>python main.py`

Watch the `data` folder for csv files being written.  

Enjoy!

If you get use out of this, let me know!
