# CS110Exam_Colwell,Andrew_C_Block.py
# Colwell, Andrew (Jan, 2016)
'''
Pseudocode:
import random module
low score variable = 0
setup game loop
    set variables
    guesses =0
    random number between 0-9999
    loop for guesses
        userGuess
        guesses + 1
        compare userguess to random number
        if guess equals random number
            check for lowscore
            if new lowscore, reset to users guesses
            reset to end guess loop
            tell user they won
        if low tell user guess is low
        if high tell user guess is high
'''
import random
lowScore = 10000
gamePlay = 'y'

while gamePlay == 'y':
    numberOfGuesses = 0
    userGuess = eval(input('Input a number between 0 and 9999:'))
    compNumber = random.randint(0,9999)
    print(compNumber) #Remove after testing
    while userGuess != compNumber:
        if userGuess > compNumber:
            print('Your guess was too high.')
        elif userGuess < compNumber:
            print('Your guess was too low.')
        numberOfGuesses = numberOfGuesses + 1
        userGuess = eval(input('Guess again:'))
    numberOfGuesses = numberOfGuesses +1
    print('You guessed the number correctly!')
    print('You guessed',numberOfGuesses,'times.')
    if numberOfGuesses < lowScore:
        print('You got the lowest score so far.')
        lowScore = numberOfGuesses
    else:
        print('Lowest score is',lowScore)
    gamePlay = input('Do you want to play again?(y/n)')

    
print('Thanks for playing the Number Guesser game.')
    
