# -*- coding: utf-8 -*-
import typing
from   typing import *

min_py = (3, 6)

###
# Standard imports, starting with os and sys
###
import os
import sys
if sys.version_info < min_py:
    print(f"This program requires Python {min_py[0]}.{min_py[1]}, or higher.")
    sys.exit(os.EX_SOFTWARE)

###
# Other standard distro imports
###
import argparse
import contextlib
from   datetime import date, datetime, timedelta
import getpass
mynetid = getpass.getuser()
import logging

###
# From hpclib
###
import linuxutils
from   urdecorators import trap
from   urlogger import URLogger

###
# imports and global objects that are a part of this project
###
#logger = URLogger(logfile='charge.log', level=logging.ERROR)

###
# Credits
###
__author__ = 'George Flanagin'
__copyright__ = 'Copyright 2024, University of Richmond'
__credits__ = None
__version__ = 0.1
__maintainer__ = 'George Flanagin'
__email__ = 'gflanagin@richmond.edu'
__status__ = 'in progress'
__license__ = 'MIT'

@trap
def parse_time(t:str) -> datetime.time:
    """
    Take the string t, and see if it is a datetime.time object.
    """
    try:
        return datetime.strptime(t, '%H:%M').time()
    except Exception as e:
        print(f"Invalid time format {t}. Should be [H]H:MM")
        sys.exit(os.EX_DATAERR)
    

@trap
def chargetime_main(myargs:argparse.Namespace) -> int:
    """
    Tedious ...
    """

    kwh_per_min = myargs.kw / 60
    battery_kwh_start = myargs.battery_capacity * myargs.current_charge / 100
    battery_kwh_target = myargs.battery_capacity * myargs.target_charge / 100

    kwh_needed = battery_kwh_target - battery_kwh_start
    minutes_needed = kwh_needed / kwh_per_min
    recombined = datetime.combine(date.today(), myargs.start)
    ready_at = (recombined + timedelta(minutes=minutes_needed)).time()

    print(f"Your car will be charged to {myargs.target_charge}% at {ready_at}")
    return os.EX_OK


if __name__ == '__main__':
    
    now_datetime = datetime.now()
    now_date = now_datetime.date()
    now_time = now_datetime.time()
    five_minutes_ago = (now_datetime - timedelta(minutes=5)).time()

    parser = argparse.ArgumentParser(prog="chargetime", 
        description="Chargetime calculates when your car will be changed.")

    parser.add_argument('-b', '--battery-capacity', type=float,
        default=77.5,
        help="Usable battery capacity in kWh. Defaults to 77.5 (Audi Q4 50)")

    parser.add_argument('-c', '--current-charge', type=int, 
        required=True,
        help="Current charge level in percent")

    parser.add_argument('--kw', type=float, 
        default=6.3,
        help="Charger rating in kW. Defaults to 6.3")

    parser.add_argument('-s', '--start', type=parse_time, 
        default=five_minutes_ago,
        help="The time when charging started. Defaults to five minutes ago.")
    
    parser.add_argument('-t', '--target-charge', type=int, 
        default=80,
        choices=range(10, 105, 5),
        help="Target charge level in percent. Defaults to 80.")


    myargs = parser.parse_args()

    try:
        sys.exit(globals()[f"{os.path.basename(__file__)[:-3]}_main"](myargs))

    except Exception as e:
        print(f"Escaped or re-raised exception: {e}")

