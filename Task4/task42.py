# if we know the speed and distance of a stop sign
speed = 150  # speed coming from car
distance = 120  # distance coming from detection algorithm
Stop = "1"  # stop sign detection coming from detection algorithm
print("Initial Speed: ", speed)
while 1:
    if Stop == "1":
        if speed >= 2 and distance > 20:
            t = distance / speed  # t = time
            print("Time: ", t)
            if t < 1.0:
                speed *= t
            else:
                speed -= (t / 10) * speed
        else:
            speed = 0
            print("Speed: ", speed, " Distance: ", distance)
            break
        distance -= 20  # distance coming from detection algorithm <<<<< not needed if it started coming from algo
        print("Speed: ", speed, " Distance: ", distance)
