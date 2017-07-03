#Assignment4_1
total=0
for i in range(100,150,2):
    total=total+i

print("The addition of the even numbers between 100-150 is:",total)

#Assignment4_2
lastNumber=eval(input("\nHow far do you want to add the numbers? "))
total=0
for i in range(1,lastNumber+1):
    total=total+i

print('The total for the sequence is:',total)

#Assignment4_3
lastNumber= eval(input('\nType in the nth number in the Fibonacci Sequence that you would like to know: '))
lastNum = 0
curNum = 1
nextNum = 1
#print('loop,lastNum,curNum,nextNum')
for i in range(0,lastNumber):
    nextNum = lastNum + curNum
    lastNum = curNum
    curNum = nextNum
    #print('loop num =',i,lastNum,curNum, nextNum)
    
print("The "+str(lastNumber)+'th number in the Fibbonacci Sequence is:',lastNum)

    
