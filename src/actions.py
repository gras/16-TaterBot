# 16-TaterBot actions.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from sensors import getRBUTTON
from sensors import DEBUG
from sensors import atArmLength
from sensors import onBlack

from servos import moveClaw
from servos import moveArm
from servos import moveBin
from servos import testServos

from drive import testMotors
from drive import driveTimed
from drive import drive

from wallaby import msleep
from wallaby import seconds 

import constants as c
from constants import binGrab



'''
Four piles are called Western, Northern, Southern, and Center

'''

# tests sensors and sets prime and clone values
def init():
    print("Running Tater")
    testServos()
    testMotors()
    while not getRBUTTON():
        msleep(50)
    msleep(1000)
    c.startTime = seconds()

# goes to the fist pile
def goToWestPile():
    print("goToWestPile")
    drive(95,100)
    msleep(2000)
    moveArm(c.armFront, 10)
    moveClaw(c.clawOpen,20)
    msleep(500)
    driveTimed(95, 100, 1500)

# Starts run
def grabPile():
    print("grabPile")
    moveClaw(c.clawMid, 10)
    drive(45, 50)
    moveClaw(c.clawClose, 5)
    msleep(500)
    moveArm(c.armMid, 15)
        
# Go to the bin
def goToTaterBin():
    print("goToTaterBin")
    driveTimed(95, 100, 2500)
    drive(25,30)
    while not atArmLength():
        pass
    drive(0,0)
    #driveTimed(95, 90, 3600)
        
# Places the poms in the potato bin
def deposit():
    print("deposit")
    driveTimed(0, 0, 0)
    moveArm(c.armMid, 5)
    msleep(300)
    moveClaw(c.clawMid, 10)
    msleep(300)
    moveArm(c.armMid, 15)
    msleep(300)
    moveClaw(c.clawClose, 15)
        
# Backs up from the bin, grabbing it
def backUpFromBin():
    print("backUpFromBin")
    driveTimed(-100, -50, 1500)
    driveTimed(100, 0, 750)

# After bin is grabbed, turns to pile 2 
def goToNorthernPile():
    print("goToNorhternPile")
    driveTimed(100, 90, 1500) #3500
    driveTimed(100, 70, 2250)
    driveTimed(-35, -100, 750) # driveTimed(-70, -100, 1000)
    driveTimed(-100, -100, 500)
    driveTimed(50, 100, 1000)
    driveTimed(100, 0, 250)
    moveClaw(c.clawOpen, 15)
    moveArm(c.armFront, 10)

# Grab the northern pile    
def grabNorthPile():
    print("grabNorthPile")
    driveTimed(70, 100, 1000)
    moveClaw(c.clawMid, 10)
    drive(45, 50)
    moveClaw(c.clawClose, 5)
    msleep(500)
    driveTimed(0,0,0)
    moveArm(c.armMid, 15)

# Back up to bin
def backUpToBin():
    print("backUpToBin")
    driveTimed(-90, -100, 2750)
    moveBin(binGrab, 10)
    moveArm(c.armBack, 10)
    msleep(500)
    moveClaw(c.clawMid, 15)
    msleep(500)
    moveClaw(c.clawClose, 10)
    moveArm(c.armUp, 10)
    
#turns to south and towards center pile
def turnToSouth():
    print("turnToSouth")
    drive(100, 0) 
    while not onBlack(): # wait for black
        pass
    driveTimed(70, 70, 1000)
    driveTimed(100, 0, 1100)
    moveClaw(c.clawOpen, 15)
    moveArm(c.armFront, 15)

# Grab the middle pile    
def grabMiddlePile():
    print("grabMiddlePile")
    driveTimed(70, 70, 1000)
    moveClaw(c.clawMid, 10)
    drive(50, 50)
    moveClaw(c.clawClose, 5)
    msleep(500)
    driveTimed(0,0,0)
    moveArm(c.armBack, 15)
    driveTimed(-50, -50, 500)
    moveClaw(c.clawOpen, 15)