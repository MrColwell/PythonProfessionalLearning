# 2_HeadsOrTails_Sequel.py
# by A.Colwell(July 2017)
# Professional Learning Session
# Prints results of random chosen heads or tails

# Modules
import random

# Functions
def HorT():
    result = random.choice(['heads','tails'])
    return result

# Initial variables
headsCount = 0
tailsCount = 0

if __name__ == "__main__":
    numOfFlips = input('Enter number of coin flips:')
    intFlips = int(numOfFlips)
    for flip in range(0,intFlips):
        singleFlip = HorT()
        if singleFlip == 'heads':
            headsCount = headsCount + 1
        else:
            tailsCount = tailsCount + 1

    print('Number of heads:',headsCount)
    print('Number of tails:',tailsCount)

