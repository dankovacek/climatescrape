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
