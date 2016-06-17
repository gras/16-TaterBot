# 16-TaterBot constants.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import wallaby as w

# Start light threshold
startLightThresh = 2000

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
STARBOARD_TOPHAT = 5
STARTLIGHT = 2

# DIGITAL ports
CLONE_SWITCH = 9
RBUTTON = 13

# PRIME servo positions
armFront = 120  # Arm forward on ground 
armBump = 260  # Arm clears the bump
armShovel = 0  # Pushes poms forward past bump
armMid = 590  #Arm to score at bin
armUp = 1100  # Arm at 90 degrees up
armBack = 1550  # Arm backwards
armBlock = 465  # move the block
armOver = 713  # over the block
armBlockBack = 1650  # Arm backwards with block

clawOpen = 1000  # Claw open
clawMid = 1230  # Claw mid
clawClose = 2040  # Claw closed

outriggerIn = 150
outriggerBack = 450
outriggerTurn = 450
outriggerOut = 1650 
outriggerFront = 1900
outriggerSpin = 416
outriggerFindLine = 1200
outriggerBaseReturn = 340
outriggerBin = 1080   
outriggerApproach = 1500


# PRIME analog sensors values
topHatMidValue = 2000  # value between black and white top hat values
armLength = 1000  # robot 1 claw length from bin
ceilingHeight = 700  # value of ET beneath crater rim

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
    
    clawOpen = 525  #Claw open 
    clawMid = 800
    clawClose = 1625 #Claw closed
    
    outriggerIn = 350
    outriggerSpin = 665
    outriggerTurn = 700
    outriggerApproach = 1700
    outriggerBaseReturn = 560
    outriggerOut = 1900
    outriggerFront = 2047
    outriggerBin = 1280
