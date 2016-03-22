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

# SERVO ports
ARM = 0
CLAW = 1
BIN = 3

# ANALOG ports
LINE_FOLLOWER = 0
ET = 1

# DIGITAL ports
CLONE_SWITCH = 9
RBUTTON = 13

# PRIME servo positions
armFront = 120 #Arm forward on ground 
armBump = 260 #Arm clears the bump
armShovel= 0 #Pushes poms forward past bump
armMid = 590 #540 #Arm to score at bin
armUp = 1100 #Arm at 90 degrees up
armBack = 1500 #Arm backwards
clawOpen = 0 #Claw open
clawMid = 480 #Claw mid
clawClose = 1100 #Claw closed
binGrab = 1200 #Grab bin
binRelease = 600 #Release bin

# PRIME analog sensors values
topHatMidValue = 2000 #value between black and white top hat values
armLength = 1000 #2550 #2350 #robot 1 claw length from bin


isClone = w.digital(CLONE_SWITCH)
isPrime = not isClone

if isPrime:
    print("running PRIME")
else:
    print("running CLONE!")
    RMOTOR = 3
    LMOTOR = 0
    armFront = 80 #120
    armMid = 580 #Arm to score at bin
    armUp =  1000 #Arm at 90 degrees up
    armBack =  1350 #1500 #Arm backwards
    clawOpen = 525 #356 #Claw open 
    clawClose = 1425 #1450 #Claw closed
    binGrab = 1275 #Grab bin
    binRelease = 1800 #Release bin


    
    
