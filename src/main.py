# 16-TaterBot main.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import actions as a

import sensors as sensors

def main():
    a.init()
    a.goToSouthernPile()
    a.grabPile()
    a.goToTaterBin() 
    a.deposit()
    sensors.DEBUG()
    a.backUpFromBin()
    a.goToNorthernPile() 
    
    
if __name__ == '__main__':
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()
    
    