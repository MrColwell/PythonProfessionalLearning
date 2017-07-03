#read a bunch of numbers and calculate the average
total=0
values=0
file=open(r'U:\A5_1.txt','r')

nextNum=file.readline()

while nextNum != "":
    nextNum=int(nextNum)
    total=total+nextNum
    values+=1
    nextNum=file.readline()

print('Average is:', total/values)
print(values)
