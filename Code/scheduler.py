from datetime import datetime, date
from curtain import close_curtain, open_curtain
from sunset_api import APIResponse
import time

last_data_fetch_time = None

while True:
    today = date.today()

    if today != last_data_fetch_time:
        data = APIResponse()
        last_data_fetch_time = today
        sunrise_time = datetime.fromisoformat(data['sunrise'])
        sunset_time = datetime.fromisoformat(data['sunset'])

    current_time = datetime.now(sunrise_time.tzinfo)

    if current_time >= sunrise_time and current_time < sunset_time:
        open_curtain()
    else:
        close_curtain()
    time.sleep(300)