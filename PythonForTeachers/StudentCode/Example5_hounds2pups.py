#Project2
#Hounds&Puppies.py
#Author: QQQ
'''
Marking scheme:

Does the code run:                 2/2
Code works with loops:             2/2
Random numbers, not duplicated:    2/2
Proper number of Hounds/puppies:   2/2
Your own code:                     2/2
10/10
'''

import random

hounds=0
puppies=0
counter=0
stop=0
highscore=100000000
w,x,y,z= random.sample(range(10),4)
B=[w,x,y,z]
while stop==0:
        hounds=0
        puppies=0
        userChoice= input('Type in a four digit number with no numbers repeat:')
        a=int(userChoice[0])
        b=int(userChoice[1])
        c=int(userChoice[2])
        d=int(userChoice[3])

        A=[a,b,c,d]
        B=[w,x,y,z]

        
        print(B)#when played not included

    
        if a in (A and B) :
                puppies= puppies + 1
        if b in (A and B):
                puppies= puppies + 1
        if c in (A and B):
                puppies= puppies + 1
        if d in (A and B):
                puppies= puppies + 1
        if a==w:
                hounds= hounds + 1
        if b==x:
                hounds= hounds + 1
        if c==y:
                hounds= hounds + 1
        if d==z:
                hounds=hounds + 1

        puppies= puppies- hounds

        if (hounds>1 and puppies==1):
                print(hounds,'Hounds,',puppies,'Puppy')
                counter=counter + 1
        if (hounds==1 and puppies>1):
                print(hounds,'Hound,',puppies,'Puppies')
                counter=counter + 1
        if (hounds==1 and puppies==1):
                print(hounds,'Hound,',puppies,'Puppy')
                counter=counter + 1
        if (hounds>1 and puppies>1):
                print(hounds,'Hounds,',puppies,'Puppies')
                counter=counter + 1
        if (hounds==0 and puppies==0):
                print(hounds,'Hounds,',puppies,'Puppies')
                counter=counter + 1
        if (hounds==0 and puppies>1):
                print(hounds,'Hounds,',puppies,'Puppies')
                counter=counter + 1
        if (hounds>1 and puppies==0):
                print(hounds,'Hounds,',puppies,'Puppies')
                counter=counter + 1
        if (hounds==1 and puppies==0):
                print(hounds,'Hound,',puppies,'Puppies')
                counter=counter + 1
        if (hounds==0 and puppies==1):
                print(hounds,'Hound,',puppies,'Puppy')
                counter=counter + 1
        
        if hounds==4:
                if (counter<highscore):
                        highscore=counter
                        print('You win! It took you',counter,'tries.A new high score!')
                        again= input('Play again?')
                else:
                     print('You win! It took you',counter,'tries. Highcore:',highscore)
                     again= input('Play again?')   
                if again==('Yes'):
                        w,x,y,z= random.sample(range(10),4)
                        counter=0
                if again!=('Yes'):
                        print('Thanks For Playing!')
                        stop= 1
        
 
         
