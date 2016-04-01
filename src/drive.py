# 16-TaterBot motors.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import constants as c

from sensors import onBlack 
from sensors import atArmLength
from sensors import getRBUTTON
from sensors import getET
from sensors import onBlackLineFollower
from sensors import atCeilingHeight


from wallaby import motor
from wallaby import msleep
from wallaby import ao
from wallaby import seconds

from actions import DEBUG


# tests motors
def testMotors():
    # testing motors
    outriggerOut()
    msleep(1000)
    outriggerIn()
    msleep(1000)
    drive(100, 100)
    while not onBlack(c.LINE_FOLLOWER): #wait to see line
        pass
    stop()
    msleep(300)
    driveTimed(100, -100, 500)
    drive(-100, 100)
    while not onBlack(c.LINE_FOLLOWER):
        pass
    stop()
    msleep(1000)
    outriggerOut()
    msleep(1000)
    drive(0,-75)
    while not onBlack(c.STARBOARD):
        pass
    stop()
    msleep(1000)
    drive(0, 75)
    while not onBlack(c.LINE_FOLLOWER):
        pass
    stop()
    msleep(1000)
    outriggerIn()
    msleep(1000)

def outriggerOut():
    driveMotorTimed(c.OUTRIGGER, 100, 500)
    driveMotor(c.OUTRIGGER, 10)
    
def outriggerIn():
    driveMotorTimed(c.OUTRIGGER, -100, 500)
    driveMotor(c.OUTRIGGER, -10)

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
    drive(0, 0)
    
def driveMotorTimed(motorport, speed, time):
    motor(motorport, speed)
    msleep(time)
    
def driveMotor(motorport, speed):
    motor(motorport, speed)

def driveTilLineStarboard(left, right):
    driveTilLine(c.STARBOARD, left, right)

def driveTilLine(port,left,right):
    drive(left,right)
    while not onBlack(port):
        pass
    stop()

#Follows black line on right for specified amount of time
def timedLineFollowRight(port, time):
    sec = seconds() + time
    while seconds() < sec:
        if not onBlack(port):
            driveTimed(20,90,20)
        else:
            driveTimed(90, 20, 20)
        msleep(10)
    
#Follows black line on left for specified amount of time
def timedLineFollowLeft(port, time):
    sec = seconds() + time
    while seconds() < sec:
        if not onBlack(port):
            driveTimed(90,50,20)
        else:
            driveTimed(50, 90, 20)
        msleep(10)

def timedLineFollowRightSmooth(port, time):
    sec = seconds() + time
    while seconds() < sec:
        if not onBlack(port):
            driveTimed(20,40,20)
    
        else:
            driveTimed(40, 20, 20)
    
        msleep(10)
        
#Follows black line on right until under or not under ceiling
#if findCeiling is true, will go until ET finds ceiling
def ETLineFollowRight(port, findCeiling): 
    while atArmLength() ^ findCeiling :
        if not onBlack(port):
            driveTimed(50,100,20)
        else:
            driveTimed(100, 50, 20)
        msleep(10)

# stop all motors
def stop():
    drive(0, 0)