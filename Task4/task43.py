current_speed = 40
distance_from_stop_sign = 120
stop = 1
one_time = 1
de_accelerate = 0
safty_distance = 10
while 1:
    if stop == 1:
        if one_time == 1:
            de_accelerate = (current_speed * current_speed) / (
                2 * distance_from_stop_sign - safty_distance
            )  # v2 = u2 + 2as -> a = -u2 / 2s, here v is zero
            one_time = 0
            print("Acceleration decrese by: ", de_accelerate)
        checker = current_speed - de_accelerate
        if checker < 0:
            current_speed = 0
        else:
            current_speed -= de_accelerate
        print("Speed: ", int(current_speed))
    if current_speed < 1:
        one_time = 1
        de_accelerate = 0
        break
