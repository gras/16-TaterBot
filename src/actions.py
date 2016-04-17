# 16-TaterBot actions.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from sensors import waitForButton, crossBlack
from sensors import DEBUG
from sensors import atArmLength
from sensors import onBlack
from sensors import currentTime
from sensors import wait4light
from sensors import testSensors

from servos import moveClaw
from servos import moveArm
from servos import moveOutrigger
from servos import deliverPoms
from servos import testServos
from servos import tempServos

from drive import testMotors 
from drive import turnUntilBlack
from drive import binGrabDown
from drive import driveTimed
from drive import drive
from drive import timedLineFollowRight
from drive import stop
from drive import testET
from drive import timedLineFollowLeft
from drive import binGrabUp
from drive import lineFollowUntilEndLeft
from drive import lineFollowUntilEndRight

from wallaby import msleep
from wallaby import seconds 
from wallaby import enable_servos
from wallaby import disable_servos
from wallaby import shut_down_in

import constants as c
from constants import outriggerApproach

#Four piles are called Western, Northern, Southern, and Center

# tests sensors and sets prime and clone values
def init():
    c.startTime = seconds()
    if c.isPrime:
        print "Running Tater - Prime"
    else:
        print "Running Tater - Clone"
    print c.armFront
    testSensors()
    testServos()
    testMotors()
    moveOutrigger(c.outriggerIn, 25)
    testET()
    disable_servos()
    wait4light()
    shut_down_in(119.9)
    c.startTime = seconds()
    enable_servos()

def disposeOfDirt():
    driveTimed(95, 100, 500)
    moveClaw(c.clawClose, 20)
    moveArm(c.armBack, 25)
    moveClaw(c.clawOpen, 10)
    msleep(100)
    moveClaw(c.clawMid, 15)
    
# goes to the first pile
def goToWestPile():
    print("goToWestPile")
    drive(95, 100)
    msleep(2500)
    moveArm(c.armFront, 10)
    moveClaw(c.clawOpen, 20)
    driveTimed(95, 100, 1000)
    
# Starts run
def grabWestPile():
    print("grabWestPile")
    drive(95, 100)
    moveClaw(c.clawMid, 10)
    moveClaw(c.clawClose, 4)
    moveArm(c.armMid, 15)

# Go to the bin
def goToTaterBin():
    print("goToTaterBin")
    drive(95, 100)
    moveOutrigger(outriggerApproach, 20)
    while not onBlack(c.STARBOARD_TOPHAT):
        pass
    drive(25, 30)
    while not atArmLength():
        pass
    stop()
       
# Places the poms in the potato bin
def depositWestPile():
    print("depositWestPile")
    moveArm(c.armMid, 5)
    moveClaw(c.clawMid, 10)
    msleep(400)
    moveClaw(c.clawClose, 15)
        
# Backs up from the bin
def backUpFromBin():
    print("backUpFromBin")
    driveTimed(-100, -50, 2100)
    driveTimed(100, 20, 750)
     
# Turn to north pile
def goToNorthernPile():
    print("goToNorthernPile")
    moveClaw(c.clawOpen, 30)
    if c.isPrime:
        drive(100, 90)
        while not onBlack(c.STARBOARD_TOPHAT):
            pass
        driveTimed(100, 100, 150)
        moveOutrigger(c.outriggerTurn, 20)
        drive(100, -20)
        while not onBlack(c.STARBOARD_TOPHAT):
            pass
    else:
        drive(100, 90)
        while not onBlack(c.STARBOARD_TOPHAT):
            pass
        driveTimed(100, 0, 1000)
    moveArm(c.armFront, 20)
    stop()
    
# Grab the northern pile    
def grabNorthPile():
    print("grabNorthPile")
    drive(90, 100)
    msleep(1000)
    moveClaw(c.clawMid, 10)
    drive(45, 50)
    moveClaw(c.clawClose, 4)
    stop()
    moveArm(c.armMid, 15)
    
# Grab the Bin
def grabBin():
    print("grabBin")
    moveOutrigger(c.outriggerBin, 20)
    driveTimed(0, -100, 400)
    drive(-95, -100)
    while not onBlack(c.STARBOARD_TOPHAT):
        pass
    stop()
    driveTimed(-50, -50, 150)
    binGrabUp()
    
# turns to south and towards center pile
def turnToSouth():
    print("turnToSouth")
    
    deliverPoms()
    driveTimed(100, 50, 2000) 
    drive(100, 0)
    while not onBlack(c.STARBOARD_TOPHAT):
        pass
    stop()
    if c.isPrime:
        driveTimed(100, 0, 500)
    else:
        driveTimed(100, 0, 250)
    moveOutrigger(c.outriggerOut, 100)
    
# Grab the middle pile    
def grabMiddlePile():
    print("grabMiddlePile")
    moveClaw(c.clawOpen, 25)
    moveArm(c.armFront, 25)
    drive(100, 100)
    msleep(300) 
    timedLineFollowLeft(c.STARBOARD_TOPHAT, 3)
    moveClaw(c.clawMid, 10)
    drive(60, 60) 
    moveClaw(c.clawClose, 5)
    moveArm(c.armMid, 25)
    stop()
    deliverPoms()

# Grab south pile, raising front of claw in order to pass bump  
def grabSouthPile():
    print ("grabSouthPile")
    moveClaw(c.clawOpen, 10)
    moveArm(c.armFront, 15)
    moveArm(c.armShovel, 10)
    timedLineFollowLeft(c.STARBOARD_TOPHAT, 5)
    drive(50, 50)  
    moveArm(c.armFront, 50)
    moveClaw(c.clawClose, 5)
    msleep(500)
    stop()
    moveArm(c.armMid, 15)
    deliverPoms()

# line follows to home    
def goToHome ():
    print("goToHome")
    turnUntilBlack(c.STARBOARD_TOPHAT, 100, 0)
    lineFollowUntilEndLeft(c.STARBOARD_TOPHAT)
    
    driveTimed(100, 90, 1000) #was 500
    moveOutrigger(c.outriggerSpin, 100)
    timedLineFollowRight(c.LINE_FOLLOWER, 3) #was 3.75

# Delivers bin    
def deliverBin():
    print("deliverBin")
    drive(-100, 0)
    while not onBlack(c.STARBOARD_TOPHAT):
        pass
    stop()
    driveTimed(100, 100, 500)

# Releases bin in home
def releaseBin():
    print ("releaseBin")
    moveArm(c.armUp, 15)
    binGrabDown()
    print "Dropped bin at:"
    currentTime()
    driveTimed(100, 80, 1000)
    moveOutrigger(c.outriggerIn, 100)
    
# line follows to cube    
def goToCenter():
    print("goToCenter")
    driveTimed(95, 100, 4000)
    driveTimed(100, 60, 3000)
    drive(100, 100)
    while not onBlack(c.LINE_FOLLOWER):
        pass
    drive(100, 0)
    while onBlack(c.LINE_FOLLOWER):
        pass
    stop()
    timedLineFollowRight(c.LINE_FOLLOWER, 2)
    drive(100, 100)
    moveClaw(c.clawOpen, 25)
    lineFollowUntilEndRight(c.LINE_FOLLOWER)
    if c.isPrime:
        driveTimed(90, 50, 200)
    moveArm(c.armShovel, 15)
    msleep(400)  
    driveTimed(100, 100, 1500)
    
# Grabs Cube
def grabCube():
    print("grabCube")
    moveArm(c.armUp, 10)
    drive(0, -100)
    crossBlack(c.LINE_FOLLOWER)
    moveClaw(c.clawOpen, 15)
    msleep(653)
    stop()
    moveArm(c.armFront, 15)
    driveTimed(100, 100, 1100)
    binGrabUp()
    moveClaw(c.clawClose, 10)
    
# Returns to base with pom filled bin
def returnToBase():
    print ("returntobase")
    moveArm(c.armBlockBack, 10)
    driveTimed(-100, 0, 1000)
    driveTimed(-100, -80, 7000) 
    drive(-100, -100)
    msleep(4000)
    msleep(750)
    moveOutrigger(c.outriggerBaseReturn, 20)
    msleep(300);
    while(onBlack(c.STARBOARD_TOPHAT)):
        pass
    stop()
   
def scoreCube():
    print "scoreCube"
    drive(50, 50)
    while not onBlack(c.STARBOARD_TOPHAT):
        pass
    stop()
    msleep(500)
    driveTimed(45, 50, 700)
    moveClaw(c.clawOpen, 25)
    msleep(300)
    moveArm(c.armUp, 10)
    driveTimed(100, 100, 1100)

def lineUpWithRamp():
    print("lineUpWithRamp")
    driveTimed(100, 20, 2000)
    driveTimed (0, 100, 1000)
    driveTimed(-100, -80, 4000)
    drive(-100, -20)
    moveOutrigger(c.outriggerBin, 25)
    msleep(1750)
    driveTimed(-100, -100, 3000)

def goToCenterAgain():
    print("goCenterAgain")
    driveTimed(95, 100, 3000)
    
    DEBUG() #debug here
    
    driveTimed(100, 60, 3000)
    drive(100, 100)
    while not onBlack(c.LINE_FOLLOWER):
        pass
    drive(100, 0)
    while onBlack(c.LINE_FOLLOWER):
        pass
    stop()
    timedLineFollowRight(c.LINE_FOLLOWER, 2)
    drive(100, 100)
    moveClaw(c.clawOpen, 25)
    lineFollowUntilEndRight(c.LINE_FOLLOWER)
    driveTimed(100, 0, 150)
    msleep(400)  
    driveTimed(100, 100, 1500)

def tempInit():
    c.startTime = seconds()
    tempServos()
    moveOutrigger(c.outriggerIn, 100)
    moveArm(c.armUp, 10)
    msleep(500)
    moveClaw(c.clawMid, 15)
    msleep(500)
    binGrabUp()
    waitForButton()
    c.startTime = seconds()
