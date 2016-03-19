# 16-TaterBot motors.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import constants as c

from sensors import onBlack
from sensors import getRBUTTON
from sensors import getET

from wallaby import motor
from wallaby import msleep
from wallaby import ao


# tests motors
def testMotors():
    # testing motors
    drive(100, 100)
    while not onBlack(): #wait to see line
        pass
    driveTimed(0, 0, 0)
    driveTimed(100, -100, 500)
    driveTimed(-100, 100, 400)
    print("Put your hand in front of ET")
    while getET() < 2000: 
        pass
    driveTimed(-100, -100, 1000)
    driveTimed(0, 0, 0)
    print("Press the right button to start...")
    while not getRBUTTON():
        pass

def drive(left, right):
    if c.isPrime:
        motor(c.LMOTOR,left)
        motor(c.RMOTOR,right)
    else:
        motor(c.LMOTOR,left)
        motor(c.RMOTOR,right)

def driveTimed(left,right,time):
    drive(left,right)
    msleep(time)
    ao()
    