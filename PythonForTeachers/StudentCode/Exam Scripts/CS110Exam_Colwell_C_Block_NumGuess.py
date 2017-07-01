# CS110Exam_Colwell_C_Block.py
# Colwell, Andrew (Jan, 2016)
'''
Pseudocode:
import Random
set initial variables
loop until game ends

    get random number
    loop until player stops
        get user guess
        add one to guess counter
        compare with random number
            == print number of guesses, condition to restart game
            > random number print guess too high
            < random number print guess too low
            
'''
import random

lowScore = 10000
playGame = True
guessAgain = True
guessCount = 0


while playGame == True:
    guess = input('Guess a number between 0 and 9999.')
    randNumber = random.randint(0,9999)
    while guessAgain == True:
        guessCount += 1
        guess = eval(guess)
        if guess == randNumber:
            guessAgain = False
            print('You got the number! Only took',guessCount,'tries.')
            if guessCount < lowScore:
                print('You have a new lowScore')
            else:
                print('Low score is',lowScore,'guesses.')
        elif guess > randNumber:
            print('Your guess is high.')
            guess = input('Guess a number between 0 and 9999.')
        else:
            print('Your guess is low.')
            guess = input('Guess a number between 0 and 9999.')
        
    guess = input('Guess a number between 0 and 9999 or "n" to quit.')
    if guess == 'n': playGame = False
    randNumber = random.randint(0,9999)   
    
    
        
    

    
    
