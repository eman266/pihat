#! usr/bin/env python

from sense_hat import SenseHat
import random
import time
sense= SenseHat()

r = random.randint(0,255)

print ("the random number is"), r, ("this time")

sense.set_pixel(2,5, (r, 0, 0))




time.sleep(1)
sense.clear()



