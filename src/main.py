# 16-TaterBot main.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from actions import init 
from actions import grabNorthPile
from actions import goToWestPile
from actions import grabPile
from actions import goToTaterBin
from actions import deposit
from actions import backUpFromBin
from actions import goToNorthernPile
from actions import backUpToBin
from actions import turnToSouth
from actions import grabMiddlePile
from actions import grabSouthPile

from sensors import DEBUG

def main():
    init()
    goToWestPile()
    grabPile()
    goToTaterBin() 
    deposit()
    backUpFromBin()
    goToNorthernPile()
    grabNorthPile()
    backUpToBin()
    turnToSouth()
    grabMiddlePile()
    grabSouthPile()
    DEBUG() 
    
    
if __name__ == '__main__':
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()
    
    