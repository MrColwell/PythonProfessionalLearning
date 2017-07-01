#2Windows.py
#A.Colwell (2014)
#Python 3.x

'''
This program opens two windows in graphics.py and draws
a small rectangle in both.
'''

from graphics import *

win1 =GraphWin("Window1",200,100)
win1.setBackground('blue')

win2 = GraphWin("Window2",300,200)
win2.setBackground('red')

rectULx,rectULy=20,20
pUL=Point(rectULx,rectULy)
pLR=Point(rectULx+30,rectULy+10)
rect=Rectangle(pUL,pLR)
rect.setFill('yellow')

rect.draw(win1)

rect2=rect.clone()
rect2.draw(win2)
