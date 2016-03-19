# 16-TaterBot main.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import actions as act

from sensors import DEBUG

def main():
    act.init()
    act.goToSouthernPile()
    act.grabPile()
    act.goToTaterBin() 
    DEBUG()
    act.deposit()
    act.backUpFromBin()
    act.goToNorthernPile() 
    
    
if __name__ == '__main__':
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()
    
    