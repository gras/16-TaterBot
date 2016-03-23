# 16-TaterBot servos.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import constants as c

from wallaby import set_servo_position
from wallaby import msleep
from wallaby import enable_servos
from wallaby import get_servo_position
from wallaby import ao

# tests servos
def testServos():
    print "Testing servos"
    set_servo_position(c.ARM, c.armUp)
    set_servo_position(c.CLAW, c.clawClose)
    set_servo_position(c.BIN, c.binRelease)
    enable_servos()
    msleep(1000)
    moveArm(c.armUp, 15)
    moveClaw(c.clawOpen, 25)
    msleep(500)
    moveClaw(c.clawClose, 25)
    msleep(500)
    moveArm(c.armFront, 15)
    moveClaw(c.clawMid, 25)
    msleep(500)
    moveClaw(c.clawClose, 25)
    msleep(500)
    moveBin(c.binGrab, 25)
    msleep(500)
    moveBin(c.binRelease, 25)
    msleep(500)
    moveArm(c.armBack, 15)
    msleep(1000)
  
def deliverPoms():  
    moveArm(c.armBack, 10)
    msleep(500)
    moveClaw(c.clawMid, 15)
    msleep(500)

    
def moveArm( endPos, speed=10 ):
    moveServo( c.ARM, endPos, speed )

def moveClaw( endPos, speed=10 ):
    moveServo( c.CLAW, endPos, speed )

def moveBin( endPos, speed=10 ):
    moveServo( c.BIN, endPos, speed )


def moveServo( servo, endPos, speed=10 ) :
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = get_servo_position( servo )
    if now > 2048 :
        PROGRAMMER_ERROR ("Servo setting too large")
    if now < 0 :
        PROGRAMMER_ERROR ("Servo setting too small")
    if now > endPos:
        speed = -speed
    for i in range (now, endPos, speed ):
        set_servo_position( servo, i)
        msleep(10)
    set_servo_position( servo, endPos )
    msleep(10)  
    
def PROGRAMMER_ERROR( msg ) :
    ao()
    print msg
    exit()  