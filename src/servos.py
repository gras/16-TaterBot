# 16-TaterBot servos.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''
import constants as c

import wallaby as w

# tests servos
def testServos():
    print "Testing servos"
    
    w.set_servo_position(c.ARM, c.armUp)
    w.set_servo_position(c.CLAW, c.clawClose)
    w.set_servo_position(c.BIN, c.binRelease)
    w.enable_servos()
    w.msleep(1000)
    moveArm(c.armUp, 25)
    w.msleep(500)
    moveArm(c.armFront, 10)
    w.msleep(500)
    moveClaw(c.clawOpen, 25)
    w.msleep(500)
    moveClaw(c.clawClose, 25)
    w.msleep(500)
    moveBin(c.binGrab, 25)
    w.msleep(500)
    moveBin(c.binRelease, 25)
    w.msleep(500)
    moveArm(c.armUp, 25)
    w.msleep(500)
    
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