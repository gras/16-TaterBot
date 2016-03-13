# main.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import actions as act
import constants as c
import wallaby as w
import helpers as h

def main():
    print 'Hello Tater\n'
    act.init()
    act.pile1()
    h.DEBUG()
    act.grabPile()
    act.goToBin1()
    act.deposit()
    act.backUpFromBin()
    act.driveToFirstGreenPile()
    
    
if __name__ == '__main__':
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()
    
# Test Servo Function
def testServo():
    w.set_servo_position(c.CLAW, c.OPEN)
    w.set_servo_position(c.CLAW, c.CLOSE)
    