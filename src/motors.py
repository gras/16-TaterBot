# 16-TaterBot motors.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from constants import LMOTOR
from constants import RMOTOR
from constants import isPrime

from wallaby import motor
from wallaby import msleep
from wallaby import ao
from helpers import getRBUTTON
from helpers import getET

# tests motors
def testMotors():
    print("Testing motors\n")
    driveTimed(100, 100, 1000)
    driveTimed(0, 0, 0)
    print("right turn\n")
    driveTimed(-100, 100, 500)
    print("left turn\n")
    driveTimed(100, -100, 400)
    print("Put your hand in front of me plz\n")
    while getET < 2000: # Doesn't work  now ***********************
        pass
    driveTimed(-100, -100, 1000)
    driveTimed(0, 0, 0)
    print("Thanks!\n Press the right button to start...\n")
    while not getRBUTTON():
        pass

def drive(left, right):
    if isPrime:
        motor(LMOTOR,left)
        motor(RMOTOR,right)
    else:
        motor(LMOTOR,left)
        motor(RMOTOR,right)

def driveTimed(left,right,time):
    drive(left,right)
    msleep(time)
    ao()
    