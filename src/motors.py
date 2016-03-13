#motors.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import constants as c
import wallaby as w

# tests motors
def testMotors():
    print("Testing motors\n")
    driveTimed(100, 100, 1000)
    driveTimed(0, 0, 0)
    print("right turn\n")
    driveTimed(-100, 100, 500)
    print("left turn\n")
    driveTimed(100, -100, 400)
    print("Put your hand in front of me plz\n")
    while w.analog(c.ET) < 2000:
        pass
    driveTimed(-100, -100, 1000)
    driveTimed(0, 0, 0)
    print("Thanks!\n Press the right button to start...\n")
    while not w.digital(c.RBUTTON):
        pass

def drive(left, right):
    if c.isPrime:
        w.motor(c.LMOTOR,left)
        w.motor(c.RMOTOR,right)
    if c.isClone:
        w.motor(c.LMOTOR,left)
        w.motor(c.RMOTOR,right)

def driveTimed(left,right,time):
    drive(left,right)
    w.msleep(time)
    w.ao()
    