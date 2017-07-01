#collisionChecker.py
#A.Colwell (2014)

'''
This script checks to see if an object has collided with another.
It uses simple distance check from centers, so it is not pixel perfect!
The Python shell window will scroll so you  can see new collisions.
'''

from graphics import *
from time import sleep

#Initial values
winX,winY=600,400           #Window Size                  
boxX=50                 
boxY=50
circleR=25
bdx,bdy=10,0                #set box motion horizontal
cdx,cdy=0,15                #set circle motion vertical
colDist=45                  #collision distance between centers

#Main Program

collided=False
window=GraphWin('Collision Detector',winX,winY)
box=Rectangle(Point(winX/4,winY/4),Point(winX/4+boxX,winY/4+boxY))
box.setFill('gray')
box.draw(window)
circle=Circle(Point(winX/2,winY/2),circleR)
circle.setFill('maroon')
circle.draw(window)

def mover(thing,dx,dy):
    thing.move(dx,dy)
    c=thing.getCenter()
    if c.getX()<25 or c.getX()>winX-25:     #bounce off walls
        dx=dx*-1
    if c.getY()<25 or c.getY()>winY-25:
        dy=dy*-1
    return dx,dy

def collision(thing1,thing2):
    c1=thing1.getCenter()
    c1x=c1.getX()
    c1y=c1.getY()
    c2=thing2.getCenter()
    c2x=c2.getX()
    c2y=c2.getY()
    if abs(c1x-c2x) < colDist and abs(c1y-c2y) < colDist:
        collided=True
    else:
        collided=False
    return collided


while window.isOpen() == True:
    cdx,cdy=mover(circle,cdx,cdy)
    if collision(circle,box) == True:
        print('Circle collided with box')
    bdx,bdy=mover(box,bdx,bdy)
    if collision(box,circle) == True:
        print('Box collided with circle')
    else:
        print('')

    sleep(.1)
    
    
