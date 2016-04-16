# 16-TaterBot main.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import actions as act

from sensors import DEBUG

def main():
    act.init()
    act.disposeOfDirt()
    act.goToWestPile()
    act.grabWestPile()
    act.goToTaterBin() 
    act.depositWestPile()
    act.backUpFromBin()
    act.goToNorthernPile()
    act.grabNorthPile()
    act.grabBin()
    act.turnToSouth()
    act.grabMiddlePile()
    act.grabSouthPile()
    act.goToHome() 
    act.deliverBin()
    act.releaseBin()
    act.goToCenter()
    act.grabCube()
    #act.pushBot()
    act.returnToBase()
    DEBUG()
    act.scoreCube()
    DEBUG()
    act.goToCenterAgain()
    
if __name__ == '__main__':
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()