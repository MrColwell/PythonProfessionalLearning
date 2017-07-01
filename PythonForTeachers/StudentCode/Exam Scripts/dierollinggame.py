from random import randrange

def dieRoll(numDice):
    x=[]
    for i in range(numDice):
        d=randrange(1,7)
        x.append(d)
    #print(x)
    return x

def scoring(play,comp):
    if play>comp:
        print(namePlayer+' wins with '+str(playRoll),'George only rolled '+str(compRoll))
    elif play<comp:
        print('George wins with '+str(compRoll), 'you only rolled '+str(playRoll))
    else:
        print('TIE...  oh no.')
        print(str(playRoll),str(compRoll))
    print(namePlayer+': '+str(playScore)+'\nGeorge: '+str(compScore))
    return

print('Welcome to Dice Roller!\n'+
      'You will roll two dice against the computer.\n'+
      'The player with the highest sum wins the round.\n'+
      'The computer\'s name is George.\n')

namePlayer=input('Please enter your name:')
keepGoing = True
compScore=0
playScore=0

while keepGoing == True:

    compRoll = sum(dieRoll(2))
    playRoll = sum(dieRoll(2))

    if playRoll > compRoll:
        playScore+=1
        scoring(1,0)
    elif playRoll < compRoll:
        compScore+=1
        scoring(0,1)
    else:
        scoring(0,0)
        pass

    if compScore>4 or playScore>4:
        if compScore>4:
            print('Computer Won!')
            compScore=0
            playScore=0
        else:
            print('You Won!')
            compScore=0
            playScore=0
            
        x=input('Play again? (y/n):')

        if x == 'y':
              keepGoing = True
        else:
              keepGoing = False

    if keepGoing==True:
        x=input('Press Enter Key for next roll\n')
        
print('Ok, thanks for playing.')
                
        
    
