#ChickenCrossing.py
#A.Colwell(2016)

'''
Set up function to represent crossing a lane with argument of
how many chickens to pass.

repeat eight times starting with 1000 chickens.
store the result in a list.
print out list results.
'''

import random

def chickenCrossing(chicks):
    died = int(round(random.randint(0,chicks)*.1))
    survived = chicks - died
    #print(died)
    return survived

for x in range(9):
    survivors = [1000]
    for i in range(8):
        chickens = survivors[i]
        survived = chickenCrossing(chickens)
        survivors.append(survived)
        #print(survivors)
        
    print('Starting with 1000 chickens, the number surviving crossing each lane:')

    for i in range(1,9):
        print('Survived lane ',i,' were ',survivors[i],' representing ',
              (survivors[i])//10,'% of original flock.',sep='')
    print('With',survivors[-1],'successfully crossing the road.')
    print('Meaning that only ',(survivors[i])//10,'% of the chickens survived.\n',sep='')
    

