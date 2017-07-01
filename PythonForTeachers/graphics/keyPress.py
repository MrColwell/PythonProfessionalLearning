from graphics2 import *
from time import sleep

w = GraphWin('Button Press', 300,200)

t = Text(Point(150, 100),'Press Key')
t.draw(w)

while w.isOpen()==True:
    keyPress=w.checkKey()
    t.setText(keyPress)
    sleep(1)
