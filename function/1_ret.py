"""
The ret.py script shows how to work with
functions in Python. 
Author: Najeeb Choudhary
Python, 2017
"""


def showModuleName():

    print(__doc__)


def getModuleFile():

    return __file__


a = showModuleName()
b = getModuleFile()

print(b,a)
