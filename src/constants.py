# 16-TaterBot constants.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import wallaby as w

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
STARBOARD_TOPHAT = 5

# DIGITAL ports
CLONE_SWITCH = 9
RBUTTON = 13

# PRIME servo positions
armFront = 120 # Arm forward on ground 
armBump = 260 # Arm clears the bump
armShovel= 0 # Pushes poms forward past bump
armMid = 590 # 540 #Arm to score at bin
armUp = 1100 # Arm at 90 degrees up
armBack = 1600 # Arm backwards

clawOpen = 0 # Claw open
clawMid = 480 # Claw mid
clawClose = 1100 # Claw closed

outriggerOut  = 1600
outriggerIn = 150
outriggerFront = 1900

# PRIME analog sensors values
topHatMidValue = 2000 # value between black and white top hat values
armLength = 1000 # 2550 # 2350 #robot 1 claw length from bin
ceilingHeight = 700 #value of ET beneath crater rim

isClone = w.digital(CLONE_SWITCH)
isPrime = not isClone

if isPrime:
    print("running PRIME")
else:
    print("running CLONE!")
    armFront = 80
    armMid = 580 #Arm to score at bin
    armUp =  1000 #Arm at 90 degrees up
    armBack =  1550 #1500 #Arm backwards
    
    clawOpen = 525 #356 #Claw open 
    clawMid = 800
    clawClose = 1525 #1450 #Claw closed
    
    outriggerOut  = 1450
    outriggerIn = 350
    outriggerFront = 2047

    
#    binGrab = 1200 #Grab bin
#    binRelease = 700 #Release bin



    
    
