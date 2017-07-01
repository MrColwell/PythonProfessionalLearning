# simpleMove.py
# A. Colwell (Nov, 2016)

from graphics2 import *

# initialize window
winX=600
winY=400
gameWindow = GraphWin(title='Simple movement',width=winX,height=winY)

# initialize object to move
cX = winX/2
cY = winY/2
radius = 20
c = Circle(Point(cX,cY),radius)
c.draw(gameWindow)

while gameWindow:
    k = gameWindow.checkKey()
    if k == 'Right':
        c.move(2,0)      # move right 2 pixels
    elif k == 'Left':
        c.move(-2,0)
    elif k == 'Up':
        c.move(0,-2)
    elif k == 'Down':
        c.move(0,2)
    else:
        c.move(0,0)
