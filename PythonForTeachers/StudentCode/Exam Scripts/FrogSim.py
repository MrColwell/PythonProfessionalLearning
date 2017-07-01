#FrogSim.py
#A.Colwell (2016)

import random

def randomJump():
    rj = (random.sample(('N','S','E','W'),1))
    return rj[0]
'''
rjx = randomJump()
print(type(rjx[0]))
print(rjx[0])
'''

survived = 0

for i in range(1000):

    direction =[0,0,0,0]    #N,S,E,W


    for x in range(5):
        rjx = randomJump()
        
        if rjx == 'N':
            direction[0] = direction[0]+1
        elif rjx == 'S':
            direction[1] = direction[0]+1
        elif rjx == 'E':
            direction[2] = direction[0]+1
        elif rjx == 'W':
            direction[3] = direction[0]+1
        else:
            print(rjx)
        #print(direction)    
    for item in direction:
        if item >= 3:
            survived = survived + 1
            

print('Of the 1000 frogs simulated, there were',survived,'frogs that survived.')
print('This represents a survival rate of ',round(survived/10),'%.\n',sep='')

print('     @..@          <O)\n'+
      '     (--)          /))\n'+
      '    (>__<)        ==#==\n'+
      '    ^^~~^^')

       
