# 16-TaterBot helpers.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from wallaby import ao
from wallaby import digital 
from wallaby import analog 
from wallaby import seconds
from wallaby import a_button_clicked
from wallaby import b_button_clicked

import constants as c

# reads the right button
def getRBUTTON():
    return digital (c.RBUTTON)

# reads the ET sensor
def getET():
    return analog(c.ET) 

# stop program for testing
def DEBUG():
    ao()
    print 'Program stop for DEBUG\nSeconds: ', seconds() - c.startTime 
    exit(0)

def currentTime():
    print 'Current time: ', seconds() - c.startTime 

def onBlack(port):
    return analog(port) > c.topHatMidValue 

def onBlackLineFollower():
    return analog(c.STARBOARD_TOPHAT) > c.topHatMidValue

def crossBlack(port):
    while not onBlack(port): # wait for black
        pass
    while onBlack(port): # wait for white
        pass
    
def waitForButton():
    print("Press the right button to start...")
    while not getRBUTTON():
        pass
        
def atArmLength():
    return analog (c.ET) > c.armLength

def atCeilingHeight():
    return analog (c.ET) > c.ceilingHeight

def testET():
    x = analog(c.ET)
    print("ET = ",x)
    
def wait4light():
    while not calibrate(c.STARTLIGHT):
        pass
    wait4(c.STARTLIGHT)

def calibrate(port):
    print "Press A button with light on"
    while not a_button_clicked():
        pass
    lightOn = analog(port)
    print "On value =", lightOn
    if lightOn > 200:
        print "Bad calibration"
        return False
    
    print "Press B button with light off"
    while not b_button_clicked():
        pass
    lightOff = analog(port)
    print "Off value =", lightOff
    if lightOff < 3000:
        print "Bad calibration"
        return False
    
    if (lightOff - lightOn) < 2000:
        print "Bad calibration"
        return False
    c.startLightThresh = (lightOff - lightOn)/2
    print "Good calibration! ", c.startLightThresh 
    return True

def wait4(port):
    print "waiting for light!! " 
    while analog(port) > c.startLightThresh:
        pass
    