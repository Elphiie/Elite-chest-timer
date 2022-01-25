from datetime import datetime, timedelta
import re
from time import sleep

tomorrow = ''

#get dates
def get_time_now():
    global today
    today = datetime.now()
    # today = int(today.strftime('%Y%m%d%H%M%S'))
    return today

def set_time_tomorrow():
    tomorrow = datetime.now() + timedelta(hours=23, minutes=59, seconds=59, microseconds=999999)
    return tomorrow

set_time_tomorrow()

print(tomorrow)