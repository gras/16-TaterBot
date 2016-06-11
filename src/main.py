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
    act.wiggle()
    act.wiggle()
    act.wiggle()
    act.goToTaterBin() 
    DEBUG()
    act.depositWestPile()
    act.backUpFromBin()
    act.goToNorthernPile()
    '''
    act.grabNorthPile()
    act.grabBin()
    act.turnToSouth()
    act.grabMiddlePile()
    act.grabSouthPile()
    act.grabRedPom()
    act.grabComposter2()
    act.dropOffBin()
    act.grabComposter()'''
    DEBUG()
    
if __name__ == '__main__':
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()