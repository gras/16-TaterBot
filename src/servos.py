# 16-TaterBot servos.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
from constants import ARM
from constants import FRONT
from constants import CLAW
from constants import CLOSE
from constants import BIN
from constants import RELEASE
from constants import UP
from constants import OPEN
from constants import GRAB

import wallaby as w

# tests servos
def testServos():
    print "Testing servos"
    w.set_servo_position(ARM, FRONT)
    w.set_servo_position(CLAW, CLOSE)
    w.set_servo_position(BIN, RELEASE)
    w.enable_servos()
    w.msleep(1000)
    moveArm(UP, 10)
    moveClaw(OPEN, 10)
    w.msleep(500)
    moveClaw(CLOSE, 10)
    w.msleep(500)
    moveArm(FRONT, 10)
    w.msleep(500)
    moveBin(GRAB, 10)
    w.msleep(500)
    moveBin(RELEASE, 10)
    w.msleep(500)
    moveArm(UP, 10)
    w.msleep(500)
    
def moveArm( endPos, speed=10 ):
    moveServo( ARM, endPos, speed )

def moveClaw( endPos, speed=10 ):
    moveServo( CLAW, endPos, speed )

def moveBin( endPos, speed=10 ):
    moveServo( BIN, endPos, speed )


def moveServo( servo, endPos, speed=10 ) :
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = w.get_servo_position( servo )
    if now > 2048 :
        PROGRAMMER_ERROR ("Servo setting too large")
    if now < 0 :
        PROGRAMMER_ERROR ("Servo setting too small")
    if now > endPos:
        speed = -speed
    for i in range (now, endPos, speed ):
        w.set_servo_position( servo, i)
        w.msleep(10)
    w.set_servo_position( servo, endPos )
    w.msleep(10)  
    
def PROGRAMMER_ERROR( msg ) :
    w.ao()
    print msg
    exit()  