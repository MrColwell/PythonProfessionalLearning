#showCheckMouse.py
#A.Colwell (2014)
#Python 3.x
'''
This script shows the x,y coordinates from check mouse.
'''
#Modules to Import
from graphics import *
from time import sleep

#Initial values
winX,winY=600,400           #Window Size
window=GraphWin('Position Checker',winX,winY)
t=Text(Point(300,15),'Click in Window to show Point')
t.draw(window)
#Main Program
while window.isOpen() == True:
    
    m=window.checkMouse()
    if m != None:
        mx=m.getX()
        my=m.getY()
        if my>20:
            
            r=Text(Point(mx,my-14),'('+str(mx)+','+str(my)+')')
        else:
            r=Text(Point(mx,my+14),'('+str(mx)+','+str(my)+')')
        r.draw(window)
        p=Circle(Point(mx,my),2)
        p.draw(window)

    sleep(.01)
