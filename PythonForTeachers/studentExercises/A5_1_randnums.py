#100randomMarks.py
#Creates a 100 random marks between 60 and 100

from random import randrange

nums=[]
for i in range(100):
    r=randrange(60,100)
    nums.append(r)

f=open(r'C:\1Andrews Files\CS110\Projects\A5_1.txt','w')
for i in nums:
    f.write(str(nums[i])+'\n')

f.close()

print('100 marks printed to A5_1.txt')
