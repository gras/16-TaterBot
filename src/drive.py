# 16-TaterBot motors.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import constants as c

import sensors as sensors

from wallaby import motor
from wallaby import msleep
from wallaby import ao
from sensors import getRBUTTON
from sensors import getET

# tests motors
def testMotors():
    # testing motors
    drive(100, 100)
    while not sensors.onBlack(): #wait to see line
        pass
    driveTimed(0, 0, 0)
    driveTimed(-100, 100, 500)
    driveTimed(100, -100, 400)
    print("Put your hand in front of ET")
    while getET() < 2000: 
        pass
    driveTimed(-100, -100, 1000)
    driveTimed(0, 0, 0)
    print("Press the right button to start...")
    while not getRBUTTON():
        pass

def drive(left, right):
<<<<<<< HEAD
    if isPrime:
=======
    if sensors.isPrime:
>>>>>>> branch 'master' of ssh://git@github.com/gras/16-TaterBot.git
        motor(c.LMOTOR,left)
        motor(c.RMOTOR,right)
    else:
        motor(c.LMOTOR,left)
        motor(c.RMOTOR,right)

def driveTimed(left,right,time):
    drive(left,right)
    msleep(time)
    ao()
    