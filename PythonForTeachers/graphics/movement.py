#movement.py
#A.Colwell (2014)

from graphics2 import *
from time import sleep

#Initial values
winX,winY=600,400           #Window Size
x,y=0,0                     #Movement when no key is pressed
speed=10                    #Amount of movement
boxWidth=50                 
boxHeight=50
xDir = 10

#Main Program
window=GraphWin('Check for None',winX,winY)
text=Text(Point(winX/2,12),'Press Enter to Center')
text.draw(window)
box=Rectangle(Point(winX/2-boxWidth/2,winY/2-boxHeight/2),
              Point(winX/2+boxWidth/2,winY/2+boxHeight/2))
box.draw(window)

while window.isOpen() == True:
    center = box.getCenter()
    xValue = center.getX()
    if (xValue > winX-25) or (xValue < 25):
        xDir = xDir * -1

    box.move(xDir,0)
    sleep(.1)
    

print('All Done!')
    
