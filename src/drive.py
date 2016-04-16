# 16-TaterBot motors.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import constants as c

from sensors import onBlack 
from sensors import atArmLength
from sensors import getET

from wallaby import motor
from wallaby import msleep
from wallaby import seconds

# tests motors
def testMotors():
    drive(100, 100)
    while not onBlack(c.LINE_FOLLOWER): #wait to see line
        pass
    stop()
    drive(75,0)
    while not onBlack(c.STARBOARD_TOPHAT):
        pass
    stop()
    drive(-75, 0)
    while not onBlack(c.LINE_FOLLOWER):
        pass
    msleep(100)
    stop()
      
def binGrabUp():
    driveMotorTimed(c.BIN, 55, 600)
    driveMotor(c.BIN, 10)
    
def binGrabDown():
    driveMotorTimed(c.BIN, -100, 500)
    driveMotor(c.BIN, -10)
    
def testET():
    print("Put your hand in front of ET")
    i = 0
    while getET() >= 2000:
        print "BLOCKED!"
        msleep(333)
    binGrabDown()
    msleep(300)
    binGrabUp()
    msleep(300)
    while getET() < 2000: 
        if i > 0:
            binGrabUp()
            i = 0
        else:
            binGrabDown()
            i = 1
        msleep(300)
    binGrabDown()
    driveTimed(-100, -100, 1000)
    stop()
   
# start left & right motors
def drive(left, right):
    motor(c.LMOTOR,left)
    motor(c.RMOTOR,right)

# power and time of motors
def driveTimed(left,right,time):
    drive(left,right)
    msleep(time)
    drive(0, 0)
    
def driveTimedNoStop(left,right,time):
    drive(left,right)
    msleep(time)
    drive(0, 0)
    
def driveMotorTimed(motorport, speed, time):
    motor(motorport, speed)
    msleep(time)
    
def driveMotor(motorport, speed):
    motor(motorport, speed)

def driveTilLineStarboard(left, right):
    driveTilLine(c.STARBOARD_TOPHAT, left, right)

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
    
#Follows black line on right for specified amount of time BACKWARDS....
def timedLineFollowRightBack(port, time):
    sec = seconds() + time
    while seconds() < sec:
        if not onBlack(port):
            driveTimed(-20,-90,20)
        else:
            driveTimed(-90, -20, 20)
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
        
def timedLineFollowLeftSmooth(port, time):
    sec = seconds() + time
    while seconds() < sec:
        if onBlack(port):
            driveTimed(20,40,20)
        else:
            driveTimed(40, 20, 20)
        msleep(10)
        
def lineFollowUntilEndLeft(port):
    i = 0
    while (i < 10):
        if onBlack(port):
            i = 0
            driveTimed(50, 90, 20)
        else:
            i = i + 1
            driveTimed(90, 50, 20)

def lineFollowUntilEndRight(port):
    i = 0
    while (i < 10):
        if not onBlack(port):
            driveTimed(50, 90, 20)
            i = i + 1
        else:
            i = 0
            driveTimed(90, 50, 20)

def turnUntilBlack(port, left, right):
    drive(left, right)
    while (not onBlack(port)):
        pass
    stop()

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