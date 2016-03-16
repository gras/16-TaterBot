# 16-TaterBot motors.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from constants import LMOTOR
from constants import RMOTOR

from sensors import isPrime

from wallaby import motor
from wallaby import msleep
from wallaby import ao
from sensors import getRBUTTON
from sensors import getET

# tests motors
def testMotors():
    # testing motors
    driveTimed(100, 100, 1000)
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
    