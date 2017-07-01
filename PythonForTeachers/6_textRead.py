# 6_textRead.py
# Andrew Colwell (July 2017)

fileName = r"example.txt"
#method 1
'''
with open(fileName,'r') as myFile:
    print(myFile.read())
myFile.close()
'''

#method 2    
'''
lineNumber = 0
with open(fileName, 'r') as myFile:
    x = myFile.readline().strip()
    while x!="":
        lineNumber +=1
        print(str(lineNumber)+'.'+x)
        x = myFile.readline().strip()
myFile.close()
'''

#method 3
#'''
with open(fileName, 'r') as myFile:
    lineList = myFile.readlines()
myFile.close()
lineNumber = 0
for line in lineList:
    lineNumber +=1
    print(str(lineNumber)+'. '+line.strip())
