#A5_2.py
#Converts text to 'Dolphinese'

file=open(r'U:\A5_2.txt','r')

s=file.read()
x=s.find('\n')
L=s.split()
s1='squ'
s2='eee'
L2=[]
for item in L:
    L2.append(s1+str(item)+s2+' ')

print(''.join(L2))

    



