# 16-TaterBot motors.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import constants as c

from sensors import onBlack
from sensors import getRBUTTON
from sensors import getET
from sensors import onBlackLineFollower


from wallaby import motor
from wallaby import msleep
from wallaby import ao
from wallaby import seconds



# tests motors
def testMotors():
    # testing motors
    drive(100, 100)
    while not onBlack(): #wait to see line
        pass
    stop()
    msleep(300)
    drive(-100, -100)
    while not onBlackLineFollower(): #wait to see line
        pass
    stop()
    msleep(300)
    driveTimed(100, 100, 1000)
    driveTimed(100, -100, 500)
    driveTimed(-100, 100, 400)

def testET():
    print("Put your hand in front of ET")
    while getET() < 2000: 
        pass
    driveTimed(-100, -100, 1000)
    driveTimed(0, 0, 0)
    print("Press the right button to start...")
    while not getRBUTTON():
        pass
  
# start left & right motors
def drive(left, right):
    motor(c.LMOTOR,left)
    motor(c.RMOTOR,right)

# power and time of motors
def driveTimed(left,right,time):
    drive(left,right)
    msleep(time)
    ao()

#Follows black line on right for specified amount of time
def timedLineFollowRight(time):
    sec = seconds() + time
    while seconds() < sec:
        if not onBlack():
            driveTimed(20,90,20)
        else:
            driveTimed(90, 20, 20)
        msleep(10)
    
# stop all motors
def stop():
    ao()