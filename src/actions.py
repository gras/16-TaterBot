# 16-TaterBot actionservos.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import sensors as sensors

import servos as servos

import drive as d

from wallaby import msleep

import constants as c



'''
Four piles are called Western, Northern, Southern, and Center

'''

# tests sensors and sets prime and clone values
def init():
    print("Running Tater")
    c.setVars()
    print(c.clawOpen)
    servos.testServos()
    d.testMotors()
    while not sensors.getRBUTTON():
        msleep(50)
    msleep(1000)

# goes to the fist pile
def goToSouthernPile():
    print("goToSouthernPile")
    if sensors.isPrime():
        d.driveTimed(100, 100, 3700)
    else:
        d.driveTimed(95, 100, 3615)

# Starts run
def grabPile():
    print("grabPile")
    d.driveTimed(0,0,0)
    if sensors.isPrime():   
        servos.moveClaw(c.clawOpen, 20)
        msleep(300)
        servos.moveArm(c.armFront, 20)
        msleep(300)
        #clawClose - 100 because of issue with pushing pom out of reach
        servos.moveClaw(c.clawClose-100, 5)
        msleep(300)
        servos.moveClaw(c.clawOpen, 10)
        msleep(300)
        d.driveTimed(100, 100, 450)
        msleep(300)
        servos.moveClaw(c.clawClose, 10)
        msleep(300)
        servos.moveArm(c.armUp, 20);
        msleep(300)
    else:
        servos.moveClaw(c.clawOpen, 20)
        msleep(300)
        servos.moveArm(c.armFront, 15)
        msleep(300)
        d.driveTimed(95, 90, 250)
        msleep(200)
        servos.moveClaw(c.clawClose, 10)
        msleep(300)
        servos.moveArm(c.armUp, 5)
        msleep(300)
        
# Go to the bin
def goToTaterBin():
    print("goToTaterBin")
    if sensors.isPrime():
        d.driveTimed(95, 90, 2000)
        d.drive(30,25)
        while not sensors.atArmLength():
            pass
        d.drive(0,0)
        #driveTimed(95, 90, 3600)
    else:
        d.driveTimed(95, 100, 3700)
        
# Places the poms in the potato bin
def deposit():
    print("deposit")
    if sensors.isPrime():
        d.driveTimed(0, 0, 0)
        servos.moveArm(c.armMid, 5)
        msleep(300)
        servos.moveClaw(c.clawOpen, 10)
        msleep(300)
        servos.moveArm(c.armUp, 15)
        msleep(300)
        servos.moveClaw(c.clawClose, 15)
    else:
        d.driveTimed(0, 0, 0)
        servos.moveArm(518, 25)
        msleep(300)
        servos.moveClaw(c.clawOpen, 10)
        
# Backs up from the bin, grabbing it
def backUpFromBin():
    print("backUpFromBin")
    servos.moveArm(c.armUp, 15)
    msleep(300)
    servos.moveBin(c.binGrab, 20)
    msleep(200)
    servos.moveClaw(c.clawClose, 20)
    msleep(200)
    d.driveTimed(-95, -90, 500)

# After bin is grabbed, turns to pile 2 
def goToNorthernPile():
    print("goToNorhternPile")
    servos.moveBin(c.binRelease, 100)
    servos.moveArm(c.armUp, 20)
    msleep(200)
    servos.moveClaw(c.clawClose, 20)
    d.driveTimed(-100, 100, 300)
    d.driveTimed(95, 90, 400)
    msleep(300)
   


    