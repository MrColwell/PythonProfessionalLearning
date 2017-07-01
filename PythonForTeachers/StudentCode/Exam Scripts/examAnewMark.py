#examAnewMark.py
import random
showAgain = True
while showAgain == True:
    count = 0
    totalSum =0
    score = 0
    for x in range(1,1001):
        randomNumber= random.randint(1,9)
        if randomNumber%2 == 0:
            score = 100
        else:
            score = 60
        totalSum += score
        count += 1

    print('There were',count,'students, with an average of',round(totalSum/count,2))
    showAgain = input('Simulate again?(y/n)')
    if showAgain.lower() == 'y':
        showAgain = True
    else:
        showAgain = False

print('Thanks for simulating!')
