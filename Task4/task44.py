import time


def kiloMeter_per_hour_to_meter_per_second(current_speed):
    speed = (current_speed * 1000) / 3600
    return speed


# suppose a car speed is 70km/h when it detected stop sign , speed = (70 * 1000)m / 3600s = 19.44m/s
current_speed = kiloMeter_per_hour_to_meter_per_second(70)
distance_from_stop_sign = 120  # 120m
stop = 1
one_time = 1
de_accelerate = 0
safty_distance = 0
wait_time = 0
while 1:
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

        checker = current_speed - de_accelerate
        if checker < 0:
            current_speed = 0
        else:
            current_speed -= de_accelerate
        print("Speed: ", int(current_speed), "km/h")

        new_distance = distance_from_stop_sign - current_speed
        print("distance coverd: ", int(new_distance), "m")
        time.sleep(wait_time)
    if current_speed < 1:
        one_time = 1
        de_accelerate = 0
        break
