#A helpful little script for graphics.py module written by A.Colwell(2014)

from graphics import *

keepGoing=True

win = GraphWin('Location Identifier',600,400)
win.setBackground('white')
label = Text(Point(70,15),'Click Here to Stop')
label.draw(win)
stopper=Rectangle(Point(1,1),Point(140,25))
stopper.draw(win)


def main():
    coord=win.getMouse()
    x=coord.getX()
    y=coord.getY()
    loc = str(x)+','+str(y)
    label=Text(Point(x,y-15),loc)
    label.draw(win)
    circ=Circle(coord,3)
    circ.draw(win)
    return x,y


while keepGoing is True:
    x,y=main()
    if x<140 and y<25:
        win.close()
        break
    

    
    
    


