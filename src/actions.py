# 16-TaterBot actions.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from sensors import getRBUTTON
from sensors import isPrime
from sensors import DEBUG
from sensors import atArmLength

from servos import moveClaw
from servos import moveArm
from servos import moveBin
from servos import testServos

from drive import testMotors
from drive import driveTimed
from drive import drive

from wallaby import msleep

from constants import clawOpen 
from constants import armFront
from constants import armUp
from constants import clawClose
from constants import armMid
from constants import binGrab
from constants import binRelease
from constants import setVars



'''
Four piles are called Western, Northern, Southern, and Center

'''

# tests sensors and sets prime and clone values
def init():
    print("Running Tater")
    setVars()
    print(clawOpen)
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
        moveClaw(clawOpen, 20)
        msleep(300)
        moveArm(armFront, 20)
        msleep(300)
        moveClaw(clawClose, 5)
        msleep(300)
        moveClaw(clawOpen, 10)
        msleep(300)
        driveTimed(100, 100, 450)
        msleep(300)
        moveClaw(clawClose, 10)
        msleep(300)
        moveArm(armUp, 20);
        msleep(300)
    else:
        moveClaw(clawOpen, 20)
        msleep(300)
        moveArm(armFront, 15)
        msleep(300)
        driveTimed(95, 90, 250)
        msleep(200)
        moveClaw(clawClose, 10)
        msleep(300)
        moveArm(armUp, 5)
        msleep(300)
        
# Go to the bin
def goToTaterBin():
    print("goToTaterBin")
    if isPrime():
        driveTimed(95, 90, 2000)
        drive(30,25)
        while not atArmLength():
            pass
        drive(0,0)
        #driveTimed(95, 90, 3600)
    else:
        driveTimed(95, 100, 3700)
        
# Places the poms in the potato bin
def deposit():
    print("deposit")
    if isPrime():
        driveTimed(0, 0, 0)
        moveArm(armMid, 5)
        msleep(300)
        moveClaw(clawOpen, 10)
        msleep(300)
        moveArm(armUp, 15)
        msleep(300)
        moveClaw(clawClose, 15)
    else:
        driveTimed(0, 0, 0)
        moveArm(518, 25)
        msleep(300)
        moveClaw(clawOpen, 10)
        
# Backs up from the bin, grabbing it
def backUpFromBin():
    print("backUpFromBin")
    moveArm(armUp, 15)
    msleep(300)
    moveBin(binGrab, 20)
    msleep(200)
    moveClaw(clawClose, 20)
    msleep(200)
    driveTimed(-95, -90, 500)

# After bin is grabbed, turns to pile 2 
def goToNorthernPile():
    print("goToNorhternPile")
    moveBin(binRelease, 100)
    moveArm(armUp, 20)
    msleep(200)
    moveClaw(clawClose, 20)
    driveTimed(-100, 100, 300)
    driveTimed(95, 90, 400)
    msleep(300)
   


    