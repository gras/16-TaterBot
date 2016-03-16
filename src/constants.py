# 16-TaterBot constants.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

#from sensors import isPrime
import sensors as sensor

# MOTOR ports
RMOTOR = 0
LMOTOR = 3

# SERVO ports
ARM = 0
CLAW = 1
BIN = 3

# ANALOG ports
ET = 1

# DIGITAL ports
CLONE_SWITCH = 9
RBUTTON = 13

# PRIME servo positions
FRONT = 120 #Arm forward on ground 
MID = 580 #Arm to score at bin
UP = 1100 #Arm at 90 degrees up
BACK = 1500 #Arm backwards
OPEN = 0 #Claw open
CLOSE = 1100 #Claw closed
GRAB = 1150 #Grab bin
RELEASE = 1750 #Release bin

def setVars():
    if sensor.isPrime():
        print("running PRIME")
    else:
        print("running CLONE")
        global FRONT
        FRONT = 120
        global MID
        MID = 580 #Arm to score at bin
        global UP
        UP = 1000 #Arm at 90 degrees up
        global BACK
        BACK = 1500 #Arm backwards
        global OPEN 
        OPEN = 356 #Claw open 
        global CLOSE
        CLOSE = 1450 #Claw closed
        global GRAB
        GRAB = 1275 #Grab bin
        global RELEASE
        RELEASE = 1800 #Release bin

    
    
