#A5_1.py
#alternative but more advanced method

l1=list(int(line.strip()) for line in open(r'C:\1Andrews Files\CS110\Projects\A5_1.txt'))
ave=sum(l1)/len(l1)
print(ave)
