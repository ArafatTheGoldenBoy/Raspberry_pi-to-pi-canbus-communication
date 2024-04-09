import schedule

from datetime import datetime, timedelta
import time


def job():
    print("I'm working...")


schedule.every(2).seconds.until(timedelta(seconds=12.1)).do(job)

while True:
    schedule.run_pending()
    # time.sleep(1)
    # print("hi!")
