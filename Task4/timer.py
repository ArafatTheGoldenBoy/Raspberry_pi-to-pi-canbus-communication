from threading import Timer


def printit(val):
    Timer(val, printit, val).start()
    print("Hello, World!")


printit(0.05)
for x in range(900):
    print(x)
