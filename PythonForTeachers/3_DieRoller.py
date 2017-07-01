# 3_DieRoller.py
# by Andrew Colwell (July 2017)

import random

def dieRoller(num_dice,num_sides):
    # accepts number of dice, number of sides of each die
    # returns a list with results of each roll
    results =[]
    sides = range(1,(num_sides+1))
    
    for die in range(num_dice):
        roll = random.choice(sides)
        results.append(roll)
    return results

if __name__ == '__main__':
    print('The results of rolling two dice are:')
    print(dieRoller(2,6))
    
        
