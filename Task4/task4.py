import time
import math


def percent(val):
    val /= 100
    return val


speed = 23
Stop = "1"
step = 0
print("Initial Speed: ", speed)
while 1:
    time.sleep(1)  # to understand the log properly
    step += 1
    if Stop == "1":
        if speed >= 2:
            temp = speed * percent(70)
            speed -= math.ceil(temp)  # Each time speed reduce to 70%
        else:
            speed = 0
        print("Speed: ", speed, " Step: ", step)
