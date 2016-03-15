# 16-TaterBot actions.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import constants as c
import wallaby as w
import servos as s
import motors as m

# tests sensors and sets prime and clone values
def init():
    c.setVars()
    #Placeholder for other sensors to test
    s.testServos()
    m.testMotors()
    while not c.RBUTTON:
        w.msleep(500)
        print("End init")
    w.msleep(1000)

# Starts run
def grabPile():
    print("GRAB")
    m.driveTimed(0,0,0)
    
    if c.isClone:   # if clone
        s.moveServo(c.CLAW, c.OPEN, 20)
        w.msleep(300)
        s.moveServo(c.ARM, c.FRONT, 20)
        w.msleep(300)
        s.moveServo(c.CLAW, c.CLOSE, 10)
        w.msleep(300)
        s.moveServo(c.ARM, c.UP, 20);
        w.msleep(300)
    else:
        s.moveServo(c.CLAW, c.OPEN, 20)
        w.msleep(300)
        s.moveServo(c.ARM, c.FRONT, 15)
        w.msleep(300)
        m.driveTimed(95, 90, 250)
        w.msleep(200)
        s.moveServo(c.CLAW, c.CLOSE, 10)
        w.msleep(300)
        s.moveServo(c.ARM, c.UP, 5)
        w.msleep(300)

# Follows line. Currently obsolete as there is no tophat    
def lineTimed(time):
    end = w.seconds() + time
    while w.seconds() < end:
        if w.analog(0) < 500:
            m.driveTimed(20, 60, 0)
        else:
            m.driveTimed(60, 20, 0)
    print("line over")

# goes to the fist pile
def pile1():
    if c.isClone:
        m.driveTimed(95, 100, 3615)
    else:
        print("drive straight\n")
        m.driveTimed(100, 100, 3900)

# Go to the bin
def goToBin1():
    if c.isClone:
        m.driveTimed(95, 100, 3700) # (98,100) for clone
    else:
        m.driveTimed(95, 90, 3700)
    
# Backs up from the bin, grabbing it
def backUpFromBin():
    s.moveServo(c.ARM, c.UP, 15)
    w.msleep(300)
    s.moveServo(c.BIN, c.GRAB, 20)
    w.msleep(200)
    s.moveServo(c.CLAW, c.CLOSE, 20)
    w.msleep(200)
    m.driveTimed(-95, -90, 500)

# After bin is grabbed, turns to pile 2 
def driveToFirstGreenPile():
    s.moveBin(c.RELEASE, 100)
    s.moveServo(c.ARM, c.UP, 20)
    w.msleep(200)
    s.moveServo(c.CLAW, c.CLOSE, 20)
    m.driveTimed(-100, 100, 300)
    m.driveTimed(95, 90, 400)
    w.msleep(300)
    
# Places the poms in the potato bin
def deposit():
    if c.isClone:
        m.driveTimed(0, 0, 0)
        s.moveServo(c.ARM, 518, 25)
        w.msleep(300)
        s.moveServo(c.CLAW, c.OPEN, 10)
    else:
        m.driveTimed(0, 0, 0)
        s.moveServo(c.ARM, c.MID, 5)
        w.msleep(300)
        s.moveServo(c.CLAW, c.OPEN, 10)
        w.msleep(300)
        s.moveServo(c.ARM, c.UP, 15)
        w.msleep(300)
        s.moveServo(c.CLAW, c.CLOSE, 15)


    