# 16-TaterBot helpers.py

'''
Created on Mar 13, 2016

@author: Dead Robot Society
'''

from wallaby import ao
from wallaby import digital 
from constants import ET

def DEBUG():
    ao()
    print("Program stop for DEBUG\n")
    exit(0)
def getRBUTTON():
    return digital (13)
def getET():
    return ET 