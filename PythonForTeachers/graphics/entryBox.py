from graphics import *
from time import sleep

w=GraphWin('Entry type',600,400)
e=Entry(Point(300,200),20)
e.draw(w)
s='Entry box says:\n'
t=Text(Point(300,50),s)
t.setTextColor('darkblue')
t.draw(w)
run=1

while w.isOpen() == True:
    g=e.getText()
    t.setText(s+g)
    sleep(.1)
    

    
