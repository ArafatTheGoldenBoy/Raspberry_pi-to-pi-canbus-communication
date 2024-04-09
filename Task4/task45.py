import time
import schedule
from datetime import datetime, timedelta


def kiloMeter_per_hour_to_meter_per_second(current_speed):
    speed = (current_speed * 1000) / 3600
    return speed


def job():
    global current_speed, de_accelerate, distance_from_stop_sign
    checker = current_speed - de_accelerate
    if checker < 0:
        current_speed = 0
    else:
        current_speed -= de_accelerate
    print("Speed: ", int(current_speed), "km/h")

    new_distance = distance_from_stop_sign - current_speed
    print("distance coverd: ", int(new_distance), "m")


def schedule_task(wait_time, total_time):
    schedule.every(wait_time).seconds.until(timedelta(seconds=total_time)).do(job)


# suppose a car speed is 70km/h when it detected stop sign , speed = (70 * 1000)m / 3600s = 19.44m/s
current_speed = kiloMeter_per_hour_to_meter_per_second(70)
distance_from_stop_sign = 120  # 120m
stop = 1
one_time = 1
de_accelerate = 0
safty_distance = 0
wait_time = 0
total_time = 0

while 1:
    print("Reading from can bus every 0.2 seconds .................")
    time.sleep(0.2)
    if stop == 1:
        if one_time == 1:
            de_accelerate = (current_speed * current_speed) / (
                2 * distance_from_stop_sign - safty_distance
            )  # v2 = u2 + 2as -> a = -u2 / 2s, here v is zero
            total_time = current_speed / de_accelerate  # s
            one_time = 0
            wait_time = int(total_time) / total_time
            print(
                "Acceleration decrese by,a : ",
                de_accelerate,
                "m/s2 || Total time needed to complete,t : ",
                total_time,
                "s || Each itaration time needed to complete,tt : ",
                wait_time,
                "s",
            )
            schedule_task(wait_time, total_time)
        schedule.run_pending()

        # time.sleep(1)

    if current_speed < 1:
        time.sleep(3)
        one_time = 1
        de_accelerate = 0
        current_speed = kiloMeter_per_hour_to_meter_per_second(120)
        # break
