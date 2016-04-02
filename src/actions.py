# 16-TaterBot actions.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from sensors import waitForButton
#from sensors import getRBUTTON
from sensors import DEBUG
from sensors import atArmLength
from sensors import onBlack

from servos import moveClaw
from servos import moveArm
from servos import moveOutrigger
from servos import deliverPoms
from servos import testServos

from drive import testMotors, driveMotorTimed, binGrabUp
from drive import driveTimed
from drive import drive
from drive import timedLineFollowRight
from drive import stop
from drive import testET
from drive import timedLineFollowLeft
from drive import driveTilLineStarboard
from drive import ETLineFollowRight
from drive import timedLineFollowRightSmooth
from drive import binGrabUp

from wallaby import msleep
from wallaby import seconds 

import constants as c
#from constants import STARBOARD_TOPHAT



'''
Four piles are called Western, Northern, Southern, and Center

'''

# tests sensors and sets prime and clone values
def init():
    c.startTime = seconds()
    if c.isPrime:
        print "Running Tater - Prime"
    else:
        print "Running Tater - Clone"
    print c.armFront
    testServos()
    testMotors()
    moveOutrigger(c.outriggerIn, 15)
    testET()
    waitForButton()
    c.startTime = seconds()
    msleep(1000)
    
# goes to the fist pile
def goToWestPile():
    print("goToWestPile")
    drive(95,100)
    msleep(2000)
    moveArm(c.armFront, 10)
    moveClaw(c.clawOpen,20)
    msleep(500)
    if c.isPrime:
        driveTimed(95, 100, 1500)
    else: 
        driveTimed(95, 100, 1000)

# Starts run
def grabWestPile():
    print("grabWestPile")
    moveClaw(c.clawMid, 10)
    drive(45, 50)
    moveClaw(c.clawClose, 5)
    msleep(500)
    moveArm(c.armMid, 15)
        
# Go to the bin
def goToTaterBin():
    print("goToTaterBin")
    if c.isPrime:
        driveTimed(95, 100, 2500)
    else:
        driveTimed(95, 100, 2300)
    drive(25,30)
    while not atArmLength():
        pass
    stop()
        
# Places the poms in the potato bin
def depositWestPile():
    print("depositWestPile")
    moveArm(c.armMid, 5)
    msleep(300)
    moveClaw(c.clawMid, 10)
    msleep(500)
    moveClaw(c.clawClose, 15)
        
# Backs up from the bin
def backUpFromBin():
    print("backUpFromBin")
    driveTimed(-100, -50, 1500)
    driveTimed(100, 0, 750)

# Grab the Bin
def grabBin():
    print("grabBin")
    if c.isPrime:
        driveTimed(100, 90, 1500)
        driveTimed(100, 70, 2250)
        driveTimed(-35, -100, 750)
        driveTimed(-100, -100, 700)
    else:
        driveTimed(95, 90, 2000)
        driveTimed(100, 65, 2000) 
        driveTimed(-25, -45, 1200)
        driveTimed(-100, -100, 1000)
    driveTimed(0, 0, 500)
    binGrabUp()
    driveTimed(0, 0, 500)
     
# Turn to north pile
def goToNorthernPile():
    print("goToNorthernPile")
    if c.isPrime:
        driveTimed(50, 100, 1000)
    else:
        driveTimed(50, 100, 800)
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
    stop()
    moveArm(c.armMid, 15)
    deliverPoms()

#turns to south and towards center pile
def turnToSouth():
    print("turnToSouth")
    driveTimed(-100, -50, 3000)
    driveTimed(100,0,1000)
    msleep(500)
    moveOutrigger(c.outriggerOut, 15)
    msleep(500)
    driveTimed(100, 0, 1000)
    driveTilLineStarboard(30, 0)
    #driveTimed(-100, 0, 50)
    #driveTimed(100, 0, 100) #PRIME DOESN'T USE THIS
    

    
# Grab the middle pile    
def grabMiddlePile():
    print("grabMiddlePile")
    moveClaw(c.clawOpen, 15)
    moveArm(c.armFront, 10)
    drive(100, 100)
    timedLineFollowLeft(c.STARBOARD_TOPHAT, 2.5)# was 3
    moveClaw(c.clawMid, 10)
    drive(50, 50)
    moveClaw(c.clawClose, 5)
    msleep(500)
    stop()
    moveArm(c.armMid, 15)
    deliverPoms()

#Grab south pile, raising front of claw in order to pass bump  
def grabSouthPile():
    print ("grabSouthPile")
    moveClaw(c.clawOpen, 10)
    moveArm(c.armFront, 15)
    timedLineFollowLeft(c.STARBOARD_TOPHAT, 3)
    moveArm(c.armShovel, 10)
    timedLineFollowLeft(c.STARBOARD_TOPHAT, 2)
    drive(50, 50)#50,41
    moveArm(c.armFront, 50)
    moveClaw(c.clawClose, 5)
    msleep(500)
    stop()
    moveArm(c.armMid, 15)
    deliverPoms()

#line follows to home    
def goToHome ():
    print("goToHome")
    timedLineFollowLeft(c.STARBOARD_TOPHAT, 3)
 
#Delivers bin    
def deliverBin():
    print("deliverBin")
    driveTimed(-100, 0, 3250)#3000
    driveMotorTimed(c.OUTRIGGER, 0, 0)
    msleep(5000)
    drive(-100, -100)
    while not onBlack(c. STARBOARD_TOPHAT):
        pass
    stop()
    DEBUG()
    #driveTimed(-100, -100, 1000) 
    #driveTimed(-40, 0, 800)

#Releases bin in home
def releaseBin():
    print ("releaseBin")
    moveArm(c.armUp, 15)
    driveTimed(100, 100, 1000)
    
#line follows to cube    
def goToCube():
    print("goToCube")
    ETLineFollowRight(c.LINE_FOLLOWER, True)
    timedLineFollowRight(c.LINE_FOLLOWER, 9)
    timedLineFollowRightSmooth(c.LINE_FOLLOWER, 4)
    moveClaw(c.clawOpen, 10)
    moveArm(c.armFront, 10)
    driveTimed(70, 70, 1000)
    drive(50, 50)
    while not onBlack(c.LINE_FOLLOWER):
        pass 
    drive(0, 0)
    moveArm(c.armShovel, 10) 
    drive(50, 50)
    while onBlack(c.LINE_FOLLOWER):
        pass
    drive(0, 0)
    driveTimed(50,50,500)
    driveTimed(0,0,1000)
    driveTimed(-50,-50,500)
    moveArm(c.armUp, 15)
    moveClaw(c.clawClose, 10)
    driveTimed(70,-70,1000)

#Grabs Cube
def grabCube():
    print("grabCube")
    moveClaw(c.clawOpen, 15)
    moveArm(c.armFront, 15)
    driveTimed(100, 100, 400)
    moveClaw(c.clawClose, 10)
    moveArm(c.armUp, 10)
    
#Returns to base with pom filled bin
def returnToBase (port):
    print ("returntobase")
    driveTimed(70, 70, 1000)
    driveTimed(50, 0, 1500)
    DEBUG()
    drive(100, 100)
    while not onBlack(port): #wait to see line
        pass
    stop()
    timedLineFollowRight(5000)