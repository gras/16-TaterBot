# 16-TaterBot actions.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from sensors import waitForButton, crossBlack
from sensors import DEBUG
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

from drive import testMotors , driveTimed
from drive import turnUntilBlack
from drive import binGrabDown
from drive import driveTimed
from drive import drive
from drive import timedLineFollowRight
from drive import stop
from drive import timedLineFollowLeft
from drive import timedLineFollowBack
from drive import binGrabUp
from drive import lineFollowUntilEndLeft2
from drive import lineFollowUntilEndRight
from drive import lineFollowUntilEndRight2
from drive import testBinGrab

from wallaby import msleep
from wallaby import seconds 
from wallaby import enable_servos
from wallaby import disable_servos
from wallaby import shut_down_in

import constants as c

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
    disable_servos()
    testBinGrab()
    binGrabDown()
    msleep(500)
    print "Press and hold button."
    msleep(2000)
    waitForButton() # wait for light()
    shut_down_in(119.9)
    c.startTime = seconds()
    enable_servos()

def disposeOfDirt():
    driveTimed(95, 100, 500)
    moveClaw(c.clawClose, 20)
    moveArm(c.armMid, 25)
    msleep(100)
    #moveArm(c.armBack, 25)
    #moveClaw(c.clawOpen, 10)
    #msleep(100)
    #moveClaw(c.clawMid, 15)
    
# goes to the first pile
def goToWestPile():
    print("goToWestPile")
    drive(95, 100)
    msleep(3200)#2500
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
    moveOutrigger(c.outriggerApproach, 20)
    crossBlack(c.STARBOARD_TOPHAT, 100)
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
    if c.isPrime: #added at practice
        driveTimed(-100, -100, 250)
    else:
        pass
    driveTimed(-100, -50, 2100)
#     waitForButton()
    driveTimed(100, 20, 1100) #750 950
#     waitForButton()
    if c.isPrime:
        driveTimed(100, 100, 250) # added at practice
    else:
        pass
#     waitForButton()
     
# Turn to north pile
def goToNorthernPile():
    print("goToNorthernPile")
    moveClaw(c.clawOpen, 30)
#     waitForButton()
    drive(100, 90)
    while not onBlack(c.STARBOARD_TOPHAT):
        pass
    
#     stop()
#     waitForButton()
    
    driveTimed(100,100,150)
#     waitForButton()
    moveOutrigger(c.outriggerTurn, 200)
    msleep(200)
#     waitForButton()
    drive(100, -20)
    while not onBlack(c.STARBOARD_TOPHAT):
        pass
    
    stop()
#     waitForButton()
    
    moveArm(c.armFront, 20)
    if c.isClone:
        driveTimed(0, 100, 275) #175
    stop()
    
# Grab the northern pile    
def grabNorthPile():
    print("grabNorthPile")
    drive(90, 100)
    msleep(1500) 
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
    driveTimed(100, 0, 500)
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
    driveTimed(100, 100, 500)
#     timedLineFollowLeft(c.STARBOARD_TOPHAT, 5)
    
    drive(100, 80)
    msleep(2300)
    moveOutrigger(c.outriggerIn, 100)
    moveArm(c.armFront, 50)
    moveClaw(c.clawClose, 20)
    msleep(500)
    moveArm(c.armMid, 20)
        
#     drive(50, 50) #now same on both
#     moveArm(c.armFront, 50)
#     moveClaw(c.clawClose, 20)#5
#     msleep(500)
#     stop()
#     moveArm(c.armMid, 15)
#     deliverPoms()
#     moveOutrigger(c.outriggerFindLine, 25)

def goToBlackLine():
    while True:
        drive(100, 60)
        while not onBlack(c.LINE_FOLLOWER):
            pass
        print "black!"
        drive(50, 30)
        msleep(300)
        if onBlack(c.LINE_FOLLOWER):
            print "still black!"
            break
        print "white!"

def aroundBlock():
    print("aroundBlock")
    msleep(20)
    moveOutrigger(c.outriggerIn, 25)
    driveTimed(60, 60, 1050)
    driveTimed(60, -60, 1050)
    driveTimed(80,90,4500)
    driveTimed(65,95,4300)
    
def grabComposter():
    print("grabComposter")
    driveTimed(100, 55, 1250)
    driveTimed(50, 100, 3300)
    moveClaw(c.clawOpen, 10)
    msleep(200)
    moveArm(c.armComposter, 10)
    msleep(200)
    moveClaw(c.clawClose, 50)
    msleep(200)
    deliverPoms()
    moveArm(c.armUp, 10)
    driveTimed(-100, 100, 1400)
    binGrabDown()
#     driveTimed(100, 0, 2500)
#     moveClaw(c.clawOpen, 20)
#     msleep(300)
#     driveTimed(0, -60, 600)
#     driveTimed(40, 40, 800)
#     moveArm(c.armComposter, 8)
#     moveClaw(c.clawClose, 10)
#     moveArm(c.armUp, 10)
#     msleep(300)
    
# line follows to home    
def goToHome ():
    print("goToHome")
    drive(30, 30)
    while onBlack(c.LINE_FOLLOWER):
        pass
    
    drive(0, 30)
    while not onBlack(c.LINE_FOLLOWER):
        pass


#     timedLineFollowRight(c.LINE_FOLLOWER, .5)
    msleep(1000)
    lineFollowUntilEndRight2(c.LINE_FOLLOWER)
    driveTimed(90, 30, 400)
    deliverPoms()
    
#     moveOutrigger(c.outriggerIn, 10)
#     msleep(300)
#     driveTimed(100, 0, 900)
#     drive(100, 100)
#     crossBlack(c.LINE_FOLLOWER)
#     timedLineFollowRight(c.LINE_FOLLOWER, .3)
#     lineFollowUntilEndLeft2(c.STARBOARD_TOPHAT)
#     DEBUG()
#     driveTimed(1000, 100, 250) 
#     moveOutrigger(c.outriggerSpin, 100)
#     if c.isPrime:
#         timedLineFollowRight(c.LINE_FOLLOWER, 2.5) 
#     else:
#         timedLineFollowRight(c.LINE_FOLLOWER, 3)


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
    if c.isPrime:
        driveTimed(95, 100, 4000)
        driveTimed(100, 60, 3000) #3000
    else:
        driveTimed(90, 100, 4000)
        driveTimed(100, 60, 3000)
    drive(100, 100)
    while not onBlack(c.LINE_FOLLOWER):
        pass
    drive(100, 0)
    while onBlack(c.LINE_FOLLOWER):
        pass
    stop()
    timedLineFollowRight(c.LINE_FOLLOWER, 1) 
    drive(100, 100)
    moveClaw(c.clawOpen, 25)
    lineFollowUntilEndRight(c.LINE_FOLLOWER)
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
    msleep(500)
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
    drive(-100, -87) #-85
    while not onBlack(c.STARBOARD_TOPHAT):
        pass
    driveTimed(-100, 0, 300)
    timedLineFollowBack(c.STARBOARD_TOPHAT, 3)#2
    driveTimed(-80, -100, 1000)
    drive(-90, -100)
    msleep(3500);
    moveOutrigger(c.outriggerBaseReturn, 20)
    msleep(1000)
    while(onBlack(c.STARBOARD_TOPHAT)):
        pass
    msleep(10)
    while(onBlack(c.STARBOARD_TOPHAT)):
        pass
    msleep(10)
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
    
    DEBUG() 
    
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
