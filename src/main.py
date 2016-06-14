# 16-TaterBot main.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import actions as act
import constants as c

from sensors import DEBUG
from servos import moveClaw

def main():
    act.init()
    #act.disposeOfDirt()
    act.goToWestPile()
    act.grabWestPile()
    act.wiggle()
    act.wiggle()
    act.wiggle()
    moveClaw(c.clawClose, 10)
    act.goToTaterBin() 
    act.depositWestPile()
    act.backUpFromBin()
    act.goToNorthernPile()
    act.grabNorthPile()
    act.recollectNorthPile()
    act.grabBin()
    act.turnToSouth()
    act.grabMiddlePile()
    act.grabSouthPile()
    '''act.goToHome() 
    act.deliverBin()
    act.releaseBin()
    act.goToCenter()
    act.grabCube()
    act.returnToBase()
    act.scoreCube()
    act.attempt()
'''
    
    DEBUG()
    
if __name__ == '__main__':
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()