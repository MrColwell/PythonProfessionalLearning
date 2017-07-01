#readAtextFile.py

import os

textFile = open('NBSchools.txt', mode='r')

wholeFile = textFile.read()

print(wholeFile)
