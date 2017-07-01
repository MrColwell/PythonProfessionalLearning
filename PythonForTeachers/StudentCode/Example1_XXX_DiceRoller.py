# CS110Exam_XXX_C_Block.py
# XXX, XXX (Jan, 2016)
'''
Pseudocode:
import the random momdule
game = True
setup game loop
while game = True
    print welcome message
    ask user to input name
    set variables
    compWins = 0
    userWins = 0
    loops for roll
    while userWins does not equal 5 and while compWins does not equal 5
        compRoll = random number between 2-12
        userRoll = random number between 2-12
        if userRoll does not equal compRoll
            if userRoll is greater than compRoll
                add 1 to userWins
                tell the user they win that roll
            elif userRoll is less than compRoll
                add 1 to compWins
                tell the user that the computer won that roll
        tell the user that it is a tie and to roll again
    if compWins = 5
        tell the user that the computer won
    if userWins = 5
        tell the user that they won
    asks user to input if they want to play again or not
        game = False
game over message'''

import random                                          #imports random module

game = True                                             #used to stop game
#--------------Welcome Message---------------------
print('Welcome to the Dice Roller game!\nIn this game you will be facing off against a fierce computer name Mr.Computer.\nThe player with the highest sum win!\nMay the odds be in your favor!')
#-----------------Game Loop------------------------
while game == True:
    userName = input('Please enter your name:')

    compWins = 0
    userWins = 0
#-----------------Dice Roll Loop-------------------
    while userWins != 5 and compWins != 5:

        rollKey = input('Press enter to roll:')         #starts the roll

        compRoll = random.randint(2,12)                 #random numbers for the dice rolls
        userRoll = random.randint(2,12)

        if userRoll > compRoll:                         #if the computers roll is bigger at 1 to wins and tells user who won
            userWins = userWins +1
            print((userName),'won this roll')

        elif userRoll < compRoll:                       #if the users roll is bigger at 1 to wins and tells user who won
            compWins = compWins + 1
            print('Mr.Computer won this roll')

        elif userRoll == compRoll:                      #if the rolls are equal, reroll
            print('It was a tie, try again!')
#-----------------Game Winning Loop----------------
    if userWins == 5:                                   #if the user wins 5 rolls they win the game and tells user they won
        print((userName),'won the game!')

    elif compWins == 5:                                 #if the computer wins 5 rolls they win the game and tells user that the computer won
        print('Mr.Computer won the game!')              
#-----------------Restart--------------------------
    playagain = input('Play Again? Type yes or no:')    #prompts user to input if they want to play again

    if playagain != 'yes':                              #if answer isn't yes, game stops
        game = False
#-----------------Game Over------------------------
print('Thank you',(userName),'for playing the dice game, hope to see you soon!') #game over message
