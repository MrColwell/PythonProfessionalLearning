# rockpaperscissors.py
# Author: A.Colwell (2015)

import random

userChoice = input('Choose (R)ock (P)aper or (S)cissors')
userChoice = userChoice.lower()
compWins = 0
userWins = 0

d1 = {'r':'s','s':'p','p':'r'}

while userChoice in d1.keys():
    compChoice = random.choice(['r', 'p','s'])
    print('Computer chose',compChoice)
    if userChoice == compChoice:
        print('That was a tie!')
    elif d1[userChoice] == compChoice:
        print('You beat the computer!')
        userWins = userWins +1
    else:
        print('The computer beat you!')
        compWins = compWins +1

    if compWins == userWins:
            print('You are tied against the computer,', userWins,'to',compWins)
    elif compWins > userWins:
            print('Computer is winning,',compWins,'to',userWins)
    else:
            print('You are beating the computer,',userWins,'to',compWins)

    userChoice = input('Choose (R)ock (P)aper or (S)cissors')
    userChoice = userChoice.lower()

print('Thanks for playing!')
