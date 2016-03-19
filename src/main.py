# 16-TaterBot main.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from actions import init
from actions import goToSouthernPile
from actions import grabPile
from actions import goToTaterBin
from actions import deposit
from actions import backUpFromBin
from actions import goToNorthernPile

from sensors import DEBUG

def main():
    init()
    goToSouthernPile()
    grabPile()
    goToTaterBin() 
    deposit()
    DEBUG()
    backUpFromBin()
    goToNorthernPile() 
    
    
if __name__ == '__main__':
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()
    
    