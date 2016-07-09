# 16-TaterBot actions.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from sensors import waitForButton, crossBlack, DEBUGwithWait, PAUSE,\
    testOutriggerOut, setWait, getWait, printWait
from sensors import DEBUG
from sensors import onBlack
from sensors import currentTime
from sensors import wait4light
from sensors import testSensors
from sensors import seeObject
from sensors import testET

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
from drive import freezeMotors

from wallaby import msleep
from wallaby import seconds 
from wallaby import enable_servos
from wallaby import disable_servos
from wallaby import shut_down_in
from wallaby import freeze
import constants as c
from constants import isPrime, outriggerFindLine

#Four piles are called Western, Northern, Southern, and Center

# tests sensors and sets prime and clone values
def init():      
    c.startTime = seconds()
    if c.isPrime:
        print "Running Tater - Prime"
    else:
        print "Running Tater - Clone"
    print c.armFront
    moveArm(c.armMid, 10)
    testSensors()
    testServos()
    testMotors()
    print "testET"
    testET()
    moveArm(c.armFront, 10)
    testOutriggerOut()
    moveOutrigger(c.outriggerIn, 25)
    disable_servos()
    testBinGrab()
    binGrabDown()
    msleep(500)
    wait4light()
#     print "Press and hold button."
#     msleep(2000)
#     waitForButton()
    shut_down_in(119.9)
    c.startTime = seconds()
    enable_servos()


def getRidOfDirt():
    moveClaw(c.clawClose, 30)
    moveArm(c.armBack, 20)
    moveClaw(c.clawMid, 30)
    moveArm(c.armFront, 15)
    
#collects red pom
def disposeOfDirt():
    driveTimed(95, 100, 500)
    moveClaw(c.clawClose, 20)
    moveArm(c.armMid, 25)
    msleep(100)
    
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
    crossBlack(c.OUTRIGGER_TOPHAT, 100)
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
        driveTimed(-100, -50, 1800)
    else:
        driveTimed(-100, -100, 250)#**********************
        driveTimed(-100, -50, 1800)
    freezeMotors()
    moveOutrigger(c.outriggerNorthTurn, 40)
    drive(100, 20)
    while not onBlack(c.OUTRIGGER_TOPHAT):
        pass
    freezeMotors()
    if c.isPrime:
        driveTimed(100, 100, 250) # added at practice
    else:
        pass
        
# Turn to north pile
def goToNorthernPile():
    print("goToNorthernPile")
    moveOutrigger(c.outriggerApproachTurn, 100)
    moveClaw(c.clawOpen, 30)
    drive(100, 90)
    while not onBlack(c.OUTRIGGER_TOPHAT):
        pass
    driveTimed(100, 100, 150)
    moveOutrigger(c.outriggerNorthBack, 200)
    msleep(200)
    drive(100, -20)
    while not onBlack(c.OUTRIGGER_TOPHAT):
        pass
    stop()
    moveOutrigger(c.outriggerBack, 2000)
    moveArm(c.armFront, 20)
    stop()
    
# Grab the northern pile    
def grabNorthPile():
    print("grabNorthPile")
    if c.isPrime:
        drive(90, 100)
    else:
        drive(90, 100)#100, 85
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
    while not onBlack(c.OUTRIGGER_TOPHAT):
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
    while not onBlack(c.OUTRIGGER_TOPHAT):
        pass
    stop()
    if c.isPrime:
        driveTimed(100, 0, 500)#100,0,500
    else:
        driveTimed(80, 0, 500)
    moveOutrigger(c.outriggerOut, 100)
    
# Grab the middle pile    
def grabMiddlePile():
    print("grabMiddlePile")
    moveClaw(c.clawOpen, 25)
    moveArm(c.armFront, 25)
    drive(100, 100)
    msleep(300) 
    timedLineFollowLeft(c.OUTRIGGER_TOPHAT, 3)
    moveClaw(c.clawMid, 10)
    if c.isPrime:
        drive(60, 60)
    else:
        drive(40,40) 
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
    drive(0, 30)
    while onBlack(c.OUTRIGGER_TOPHAT):
        pass
    if c.isPrime:
        driveTimed(100, 100, 500)
    else:
        driveTimed(85, 100, 900)
    if c.isPrime:
        drive(100, 80)
    else:
        drive(100,85)
    if c.isPrime:
        msleep(1500)
    else:
        msleep(700)#850
    moveOutrigger(c.outriggerIn, 100)
    moveArm(c.armFront, 50)
    moveClaw(c.clawClose, 20)
    msleep(500)
    moveArm(c.armMid, 20)
    stop()
    deliverPoms()
    drive(-30, -30)
    if onBlack(c.LINE_FOLLOWER):
        print "on black early"
        while onBlack(c.LINE_FOLLOWER):
            pass
        freezeMotors()
#     if onBlack(c.LINE_FOLLOWER):
#         print "thats not good (265)"
#         DEBUGwithWait()
    
# goes to the black line
def goToBlackLine():
    print "goToBlackLine"
    while True:
        drive(100, 60)
        while not onBlack(c.LINE_FOLLOWER):
            pass
        print "black!"
        drive(50, 30)
        msleep(150)
        if onBlack(c.LINE_FOLLOWER):
            print "still black!"
            break
        print "white!"
    freezeMotors()
        
# line follows to home    
def goToHome (): # goes home
    print "goToHome"
    driveTimed(100, 100, 500)
    if c.isPrime:
        driveTimed(-80, 80, 2200)
    else:
        driveTimed(-80, 80, 2200)
#     driveTimed(-100, -100, 2300)
    moveOutrigger(c.outriggerCompostApproach, 1000)
    drive(-100, -100)
    msleep(2300)
    drive(-90, -100)
    msleep(400)
    setWait(4)
    while not onBlack(c.OUTRIGGER_TOPHAT) and getWait():
        pass
    while onBlack(c.OUTRIGGER_TOPHAT) and getWait():
        pass
    msleep(10)
    while onBlack(c.OUTRIGGER_TOPHAT) and getWait():
        pass
    msleep(10)
    while onBlack(c.OUTRIGGER_TOPHAT) and getWait():
        pass
    if c.isPrime:    
        driveTimed(-95, -100, 2100)
    else:
        driveTimed(-95, -100, 1800)
    binGrabDown()
    moveOutrigger(c.outriggerIn, 200)
    
    driveTimed(-100, -100, 100)
    
    driveTimed(100, 0, 4000)
    drive(0, -100)
    while not seeObject():
        pass
    freezeMotors()
    moveClaw(c.clawOpenWide, 10)
    moveArm(c.armComposter, 5)
    moveClaw(c.clawClose, 200)
    moveArm(c.armUp, 10)
    driveTimed(0, 100, 100)
    
    driveTimed(-100, -100, 750)
    driveTimed(0, 100, 1200)
    if c.isPrime:
        driveTimed(-100, -80, 1200)#750
    else:
        driveTimed(-100, -80, 900)
    deliverPoms()
    driveTimed(30, 100, 1500)
    
    
#turns in start box to grab composter
def grabComposter(): # grabs the composter
    print("grabComposter")
    if isPrime:
        driveTimed(100, 53, 1500) #1750
    else: 
        driveTimed(100, 53, 1750) #2000
    freezeMotors()
    driveTimed(42, 100, 2200)
    freezeMotors()
    findComposter() # finds the composter 
    if isPrime:
        driveTimed(45, 50, 600)
        driveTimed(-50, 50, 100)
    else:
        driveTimed(45,50,200)
        driveTimed(-50, 50, 100)
#         driveTimed(-50, -50, 300)
    freezeMotors()
    drive(100, 100)
    while not onBlack(c.LINE_FOLLOWER):
        pass
    stop()
    freezeMotors()
#   driveTimed(50, 100, 3100) #3300
    moveClaw(c.clawOpenWide, 40)
    msleep(200)
    if isPrime:
        moveArm(c.armComposter, 10)
    else:
        moveArm(c.armComposter, 10)
    msleep(200)
    moveClaw(c.clawClose, 50)#50
    msleep(200)
    moveArm(c.armUp, 10)
    driveTimed(-100, 100, 1000)
    msleep(500)
    
#puts composter in bin
def depositComposter():
    print("depositComposter")
    moveArm(c.armBlockBack, 10)
    msleep(600)
    moveClaw(c.clawOpen,40)
    msleep(200)
    binGrabDown()
    
# Delivers bin    
def deliverBin():
    print("deliverBin")
    drive(-100, 0)
    while not onBlack(c.OUTRIGGER_TOPHAT):
        pass
    stop()
    driveTimed(100, 100, 500)

# Releases bin in home
def releaseBin():
    print ("releaseBin")
    moveArm(c.armUp, 15)
    binGrabDown()
    DEBUG()
    print "Dropped bin at:"
    currentTime()
    driveTimed(100, 80, 1000)
    moveOutrigger(c.outriggerBaseReturn, 100) #outriggerIn
    
# line follows to cube    
def goToCenter():
    print("goToCenter")
    if c.isPrime:
        driveTimed(95, 100, 6000)#4000
        driveTimed(100, 60, 3000) 
    else:
        driveTimed(95, 100, 5500)#4000
        driveTimed(100, 70, 3000)
    driveTimed(100,100, 500)
    drive(100, 100)
    crossBlack(c.LINE_FOLLOWER)
    drive(80,-80)
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
    driveTimed(90, 50, 350)#400######################################################################
    moveOutrigger(c.outriggerValley, 100)
    drive(100, 100)
    while not onBlack(c.OUTRIGGER_TOPHAT):
        pass
    stop()
    moveOutrigger(c.outriggerIn, 100)
    drive(0, -100)
    while not onBlack(c.LINE_FOLLOWER):
        pass
    while onBlack(c.LINE_FOLLOWER):
        pass
    stop()
#     driveTimed(100, 100, 1500)
    
# Grabs Cube
def grabCube():
    print("grabCube")
    moveClaw(c.clawOpen, 15)
    moveArm(c.armFinalBlock, 15)
    driveTimed(80, 80, 2000)
    moveClaw(c.clawClose, 10)
    
# Returns to base with pom filled bin
def returnToBase():
    print ("returntobase")
    moveArm(c.armBlockBack, 10)
    driveTimed(-100, 0, 1000)
    driveTimed(-100, -73, 4000)
    drive(-100, -100)
    while not onBlack(c.OUTRIGGER_TOPHAT):
        pass
    while onBlack(c.OUTRIGGER_TOPHAT):
        pass
    freeze(c.LMOTOR)
    freeze(c.RMOTOR)
    drive(-80, 0)
    while not onBlack(c.LINE_FOLLOWER):
        pass    
    stop()
    moveOutrigger(c.outriggerBaseReturn, 20)
    driveTimed(-90, -100, 1000)
    drive(-90, -100)
    msleep(3500);
#     msleep(1000)
    while(onBlack(c.OUTRIGGER_TOPHAT)):
        pass
    msleep(10)
    while(onBlack(c.OUTRIGGER_TOPHAT)):
        pass
    msleep(10)
    while(onBlack(c.OUTRIGGER_TOPHAT)):
        pass
    stop()
   
def scoreCube():
    print "scoreCube"
    drive(50, 50)
    while not onBlack(c.OUTRIGGER_TOPHAT):
        pass
    stop()
    msleep(500)
    if c.isPrime:
        #driveTimed(45, 50, 600)
        setWait(.6)
        while getWait():
            dropTest()
            
    else:
        #driveTimed(45, 50, 800)#600
        setWait(.8)
        while getWait():
            dropTest()
    freezeMotors()
    moveClaw(c.clawOpen, 25)
    msleep(300)
    moveArm(c.armUp, 10)
    #driveTimed(100, 100, 1100)
    setWait(1.1)
    while getWait():
        dropTest()

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

def findComposter():
    drive(50, -50)
    while seeObject():
        pass
    freezeMotors()
    
    setWait(1.5)
    
    drive(-50, 50)
    while not seeObject() and getWait():
        pass
    freezeMotors()
    if getWait():
        time = seconds()
        drive(-50, 50)
        while not seeObject():
            pass
        drive(-50, 50)
        while seeObject():
            pass
        freezeMotors()
        time = ((seconds() - time) / 2) * 1000
        driveTimed(50, -50, int(time))

def dropTime():
    if seconds() - c.startTime > 119.25:
        return False
    return True

def dropTest():
    if dropTime():
        print ("dropTest - Cube")
        moveClaw(c.clawOpen, 10000)
        DEBUG()