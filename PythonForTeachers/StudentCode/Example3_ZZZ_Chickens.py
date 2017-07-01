# CS110Exam_ZZZ.py
# ZZZ, ZZZ (Jan,2016)
'''
Pseudocode:

define a function to simulate a chicken crossing the road
chickens=1000
lane1=(random.randint(90,100))/100
lane2=(random.randint(90,100))/100
lane3=(random.randint(90,100))/100
lane4=(random.randint(90,100))/100
lane5=(random.randint(90,100))/100
lane6=(random.randint(90,100))/100
lane7=(random.randint(90,100))/100
lane8=(random.randint(90,100))/100
chickens=chickens*lane1-8
percent=(chickens/1000)*100
print('Survived lane 1-8 were',chickens,'representing',percent,'% of original flock.)


'''
import random
chickens=1000             #sets initial amount of chickens
stop=0                    #sets up loop
lane=1                    #sets initial lane
print('Starting with 1000 chickens, the number surviving crossing each lane:')

while stop==0:           #starts loop
    if lane!=9:          #while it has not crossed all lanes
        chance=(random.randint(900,1000))/1000   #chance of 90-100% of making it
        chickens=round(chickens*chance)          #times number of chickens by chance of surving, which equals expected number of chickens that survived
        percent=str(round(chickens/1000*100))+'%' #takes percentage of how many chickens remain compared to original amount
        print('Survived lane',lane,'were',chickens,'representing',percent,'of original flock.')
        lane=lane+1                       #allows chickens to proceed to the next lane
    
    if lane==9:
        print('With',chickens,'successfully crossing the road.')
        print('Meaning that only',percent,'of the chickens survived.')
        stop=1            #stops the loop once chickens have crossed all lanes of traffic
        
        
        
    
    



