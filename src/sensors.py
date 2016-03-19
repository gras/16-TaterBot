# 16-TaterBot helpers.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from wallaby import ao
from wallaby import digital 
from wallaby import analog 

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
    print("Program stop for DEBUG\n")
    exit(0)
    
def onBlack():
    return analog(c.LINE_FOLLOWER) > c.topHatMidValue 

def atArmLength():
    return analog (c.ET) > c.armLength

def testET():
    x = analog(c.ET)
    print("ET = ",x)