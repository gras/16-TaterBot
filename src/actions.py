# 16-TaterBot actions.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from sensors import getRBUTTON
from sensors import isPrime
from sensors import DEBUG

from servos import moveClaw
from servos import moveArm
from servos import moveBin
from servos import testServos

from drive import testMotors
from drive import driveTimed

from wallaby import msleep

from constants import OPEN 
from constants import FRONT
from constants import UP
from constants import CLOSE
from constants import MID
from constants import GRAB
from constants import RELEASE
from constants import setVars



'''
Four piles are called Western, Northern, Southern, and Center

'''

# tests sensors and sets prime and clone values
def init():
    print("Running Tater")
    setVars()
    testServos()
    testMotors()
    while not getRBUTTON():
        msleep(50)
    msleep(1000)

# goes to the fist pile
def goToSouthernPile():
    print("goToSouthernPile")
    if isPrime():
        driveTimed(100, 100, 3700)
    else:
        driveTimed(95, 100, 3615)

# Starts run
def grabPile():
    print("grabPile")
    driveTimed(0,0,0)
    if isPrime():   
        moveClaw(OPEN, 20)
        msleep(300)
        moveArm(FRONT, 20)
        msleep(300)
        moveClaw(CLOSE, 5)
        msleep(300)
        moveClaw(OPEN, 10)
        msleep(300)
        driveTimed(100, 100, 450)
        msleep(300)
        moveClaw(CLOSE, 10)
        msleep(300)
        moveArm(UP, 20);
        msleep(300)
    else:
        moveClaw(OPEN, 20)
        msleep(300)
        moveArm(FRONT, 15)
        msleep(300)
        driveTimed(95, 90, 250)
        msleep(200)
        moveClaw(CLOSE, 10)
        msleep(300)
        moveArm(UP, 5)
        msleep(300)
        
# Go to the bin
def goToTaterBin():
    print("goToTaterBin")
    if isPrime():
        driveTimed(95, 90, 3600)
    else:
        driveTimed(95, 100, 3700)
        
# Places the poms in the potato bin
def deposit():
    print("deposit")
    if isPrime():
        driveTimed(0, 0, 0)
        moveArm(MID, 5)
        msleep(300)
        moveClaw(OPEN, 10)
        msleep(300)
        moveArm(UP, 15)
        msleep(300)
        moveClaw(CLOSE, 15)
    else:
        driveTimed(0, 0, 0)
        moveArm(518, 25)
        msleep(300)
        moveClaw(OPEN, 10)
        
# Backs up from the bin, grabbing it
def backUpFromBin():
    print("backUpFromBin")
    moveArm(UP, 15)
    msleep(300)
    moveBin(GRAB, 20)
    msleep(200)
    moveClaw(CLOSE, 20)
    msleep(200)
    driveTimed(-95, -90, 500)

# After bin is grabbed, turns to pile 2 
def goToNorthernPile():
    print("goToNorhternPile")
    moveBin(RELEASE, 100)
    moveArm(UP, 20)
    msleep(200)
    moveClaw(CLOSE, 20)
    driveTimed(-100, 100, 300)
    driveTimed(95, 90, 400)
    msleep(300)
   


    