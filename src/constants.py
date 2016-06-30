# 16-TaterBot constants.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import wallaby as w

# Start light threshold
startLightThresh = 2000
etObject = 2000

# TIME
startTime = -1

# MOTOR ports
LMOTOR = 0
RMOTOR = 3
BIN = 2


# SERVO ports
ARM = 0
CLAW = 1
OUTRIGGER = 3

# ANALOG ports
LINE_FOLLOWER = 0
ET = 1
OUTRIGGER_TOPHAT = 5
STARTLIGHT = 2

# DIGITAL ports
CLONE_SWITCH = 9
RBUTTON = 13

# PRIME servo positions
armShovel = 02  # Pushes poms forward past bump
armFront = 120  # Arm forward on ground 
armBump = 260  # Arm clears the bump
armBlock = 465  # move the block
armComposter = 500  # Arm to grab Composter
armMid = 630  #Arm to score at bin
armOver = 713  # over the block
armUp = 1100  # Arm at 90 degrees up
armBack = 1550  # Arm backwards
armBlockBack = 1650  # Arm backwards with block

clawOpen = 0  # Claw open
clawMid = 230  # Claw mid
clawClose = 1000  # Claw closed

outriggerIn = 250
outriggerBaseReturn = 340
outriggerSpin = 416
outriggerBack = 450
outriggerBin = 1080   
outriggerFindLine = 1200
outriggerApproach = 1500
outriggerOut = 1650 
outriggerFront = 1900
outriggerValley = 540

# PRIME analog sensors values
ceilingHeight = 700  # value of ET beneath crater rim
armLength = 1000  # robot 1 claw length from bin
topHatMidValue = 2000  # value between black and white top hat values

isClone = w.digital(CLONE_SWITCH)
isPrime = not isClone

if isPrime:
    print("running PRIME")
else:
    print("running CLONE!")
    armFront = 80
    armMid = 500  # Arm to score at bin
    armUp = 1000  # Arm at 90 degrees up
    armBack = 1500# Arm backwards
    
    clawOpen = 700  #Claw open 800 
    clawMid = 1030
    clawClose = 1840 #Claw closed
    
    outriggerIn = 100
    outriggerBaseReturn = 230 
    outriggerSpin = 315 
    outriggerBack = 335 
    outriggerBin = 950 
    outriggerFindLine = 1100
    outriggerApproach = 1400 
    outriggerOut = 1500 
    outriggerFront = 1770 
