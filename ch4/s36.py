import random

lightOn = bool(random.randint(0, 1))

if lightOn:
    print("Light is ON")

if lightOn == False:
    print("Light is OFF")