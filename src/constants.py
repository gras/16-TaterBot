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
LINE_FOLLOWER = 0

# DIGITAL ports
CLONE_SWITCH = 9
RBUTTON = 13

# PRIME servo positions
armFront = 120 #Arm forward on ground 
armMid = 540 #Arm to score at bin
armUp = 1100 #Arm at 90 degrees up
armBack = 1500 #Arm backwards
clawOpen = 0 #Claw open
clawClose = 1100 #Claw closed
binGrab = 1150 #Grab bin
binRelease = 1750 #Release bin

# PRIME analog sensors values
topHatMidValue = 2000 #value between black and white top hat values
armLength = 2550 #2350 #robot 1 claw length from bin

def setVars():
    if sensor.isPrime():
        print("running PRIME")
    else:
        print("running CLONE!")
        global RMOTOR
        RMOTOR = 3
        global LMOTOR
        LMOTOR = 0
        global armFront
        armFront = 80 #120
        global armMid
        armMid = 580 #Arm to score at bin
        global armUp
        armUp =  1000 #Arm at 90 degrees up
        global armBack
        armBack =  1350 #1500 #Arm backwards
        global clawOpen 
        clawOpen = 525 #356 #Claw open 
        global clawClose
        clawClose = 1425 #1450 #Claw closed
        global binGrab
        binGrab = 1275 #Grab bin
        global binRelease
        binRelease = 1800 #Release bin


    
    
