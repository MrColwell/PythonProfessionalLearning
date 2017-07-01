# 2_HeadsOrTails_Sequel_b.py
# by A.Colwell(July 2017)
# Professional Learning Session
# Prints results of random chosen heads or tails

# Modules
import random

# Functions
def HorT():
    result = random.choice(['heads','tails'])
    return result

def multHeadsTails(flips):
    # pass in argument of number of times to flip a coin.
    # function will return a list of number of [heads,tails]
    heads = 0
    tails = 0
    for eachflip in range(flips):
        result = HorT()
        if result == 'heads':
            heads = heads + 1
        else:
            tails = tails + 1
    return [heads, tails]
            

# Initialize variables
headsCount = 0
tailsCount = 0

if __name__ == "__main__":
    numOfFlips = input('Enter number of coin flips:')
    intFlips = int(numOfFlips)
    headsCount,tailsCount = multHeadsTails(intFlips)
    print('Number of heads:',headsCount)
    print('Number of tails:',tailsCount)

