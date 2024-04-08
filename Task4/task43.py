current_speed = 70
distance_from_stop_sign = 120
stop = 1
one_time = 1
de_accelerate = 0
safty_distance = 0
while 1:
    if stop == 1:
        if one_time == 1:
            de_accelerate = (current_speed * current_speed) / (
                2 * distance_from_stop_sign - safty_distance
            )  # v2 = u2 + 2as -> a = -u2 / 2s, here v is zero
            total_time = current_speed / de_accelerate
            one_time = 0
            print(
                "Acceleration decrese by,a : ",
                de_accelerate,
                "|| Total time needed to complete,t : ",
                total_time,
            )
        checker = current_speed - de_accelerate
        if checker < 0:
            current_speed = 0
        else:
            current_speed -= de_accelerate
        print("Speed: ", int(current_speed))

        new_distance = distance_from_stop_sign - current_speed
        print("distance coverd: ", int(new_distance))
    if current_speed < 1:
        one_time = 1
        de_accelerate = 0
        break
