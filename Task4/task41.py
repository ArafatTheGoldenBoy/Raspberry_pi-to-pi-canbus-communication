# only know the speed of the car


def percent(val):
    val /= 100
    return val


speed = 80  # speed coming from car
Stop = "1"  # stop sign detection coming from detection algorithm
step = 0
print("Initial Speed: ", speed)
while 1:
    step += 1
    if Stop == "1":
        if speed >= 2:
            speed -= speed * percent(30)  # Each time speed reduce to 70%
        else:
            speed = 0
            print("Speed: ", speed, " Step: ", step)
            break
        print("Speed: ", speed, " Step: ", step)
