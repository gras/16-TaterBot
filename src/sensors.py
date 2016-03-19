# 16-TaterBot helpers.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from wallaby import ao
from wallaby import digital 
from wallaby import analog 

from constants import ET
from constants import CLONE_SWITCH
from constants import RBUTTON
from constants import topHatMidValue
from constants import LINE_FOLLOWER
from constants import armLength

# reads the right button
def getRBUTTON():
    return digital (RBUTTON)

# reads the ET sensor
def getET():
    return analog(ET) 

# reads the clone switch
def isClone():
    return digital(CLONE_SWITCH)

# returns inverse of clone switch    
def isPrime(): 
    return not digital(CLONE_SWITCH)
    #return not isClone()

# stop program for testing
def DEBUG():
    ao()
    print("Program stop for DEBUG\n")
    exit(0)
    
def onBlack():
    return analog(LINE_FOLLOWER) > topHatMidValue 

def atArmLength():
    return analog (ET) > armLength

def testET():
    x = analog(ET)
    print("ET = ",x)