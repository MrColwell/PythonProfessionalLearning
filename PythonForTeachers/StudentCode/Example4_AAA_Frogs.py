# CS110Exam_AAA_D_Block.py
# AAA, AAA (Jan, 2016)
'''
Pseudocode:
import math
import random
set varriables
startFrogNum
frogNum

loops for the sim:
for i in range(startFrogNum):
    set a new list for every froge, l=[]
    for i in range(5):
        frogLuck=random.randint(1,4)
        l.append(frogLuck)
        assign each number(1-4) to a direction
        north= l.count(1)
        south= "      "
        east= "       "
        west= "       "
        measure distances of each direction

calculate survival rate

            
print('blahblahblahbalh', frogNumn 'blahblahblahblah', frogPercent, '%.)
print(little froggie guys)           

'''

import random
startFrogNum=1000                             #set varriables
frogSuv=0

for i in range(1000):                         #loop for main sim
    lifeLine=[]
    for i in range(5):                        #loop for each frog
        frogLuck=random.randint(1,4)
        lifeLine.append(frogLuck)
        north= lifeLine.count(1)              #counting the distance taveled
        south= lifeLine.count(2)
        east= lifeLine.count(3)
        west= lifeLine.count(4)
        if north >= 3:                        #evaluating the distance traveled
            frogSuv+=1
        if south >= 3:
            frogSuv+=1
        if east >= 3:
            frogSuv+=1
        if west >= 3:
            frogSuv+=1
suvRate=frogSuv/10
print('Of the  1000 frogs simulated, there were', frogSuv, 'frogs that survived.','\n','This represents a survival rate of', suvRate,'%.')
print('     @..@           <O)','\n','    (--)           /))','\n','   (>__<)         ==#==','\n',   '   ^^~~^^')





             
