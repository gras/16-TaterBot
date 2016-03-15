# 16-TaterBot main.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

import actions as act

from helpers import DEBUG

def main():
    print 'Hello Tater\n'
    act.init()
    act.pile1()
    act.grabPile()
    act.goToBin1()
    act.deposit()
    act.backUpFromBin()
    act.driveToFirstGreenPile()
    DEBUG()
    
    
if __name__ == '__main__':
    # set print to unbuffered
    import os
    import sys
    sys.stdout = os.fdopen(sys.stdout.fileno(),'w',0)
    main()
    
    