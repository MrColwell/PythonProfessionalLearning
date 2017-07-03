#A5_3 Read three points from a text file
#Then draw the triangle with graphics.py

from graphics import *
from time import sleep

#file=open(r'A5_3.txt','r')
file=open(r'U:\trianglePoints.txt','r')

L1=[]
data=file.readline()

while data !='':

    s=data.find('\n')       
    if s>=0:                #If there is an \n,
        data=data[:s]       #strip off the escape code
    l=data.split(',')       #split the data into nested lists
    L1.append(l)            #build L1 as the list with numbers as strings
    data=file.readline()

print('Preparing to print a triangle. Hold on to your hats!')
print(L1)
sleep(3)

win=GraphWin('Draw a triangle',300,300)
p1=Point(int(L1[0][0]),int(L1[0][1]))   #Make points integers from strings
p2=Point(int(L1[1][0]),int(L1[1][1]))
p3=Point(int(L1[2][0]),int(L1[2][1]))

triangle=Polygon(p1,p2,p3)
triangle.setFill('green')
triangle.draw(win)

file.close()
print('All done! Hold your applause for later.')

