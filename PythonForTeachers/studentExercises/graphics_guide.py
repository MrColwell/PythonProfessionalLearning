#A helpful little script by A. Colwell (2014).

from graphics import *

win1 = GraphWin('graphics.py Guide',600,400)

circ = Circle(Point(50,30),25)
circ.draw(win1)
labelCirc = Text(Point(200,25),'Circle at 50,30 with radius of 25')
labelCirc.draw(win1)
lineCirc = Line(Point(75,55),Point(50,30))
lineCirc.setFill('red')
lineCirc.setArrow('last')
lineCirc.draw(win1)

rect = Rectangle(Point(20,100),Point(60,140))
rect.draw(win1)
labelRect = Text(Point(250,120),'Rectangle UpLeft(20,100),LowRight(60,140)')
labelRect.draw(win1)
line1Rect = Line(Point(20,70),Point(20,100))
line1Rect.setFill('red')
line1Rect.setArrow('last')
line1Rect.draw(win1)
line2Rect = Line(Point(90,140),Point(60,140))
line2Rect.setFill('red')
line2Rect.setArrow('last')
line2Rect.draw(win1)

labelOval = Text(Point(250,240),'Oval UpLeft(20,200),LowRight(60,280)')
labelOval.draw(win1)
line1Oval = Line(Point(20,180),Point(20,200))
line1Oval.setFill('red')
line1Oval.setArrow('last')
line1Oval.draw(win1)
line2Oval = Line(Point(90,280),Point(60,280))
line2Oval.setFill('red')
line2Oval.setArrow('last')
line2Oval.draw(win1)
rectOval = Rectangle(Point(20,200),Point(60,280))
rectOval.setOutline('red')
rectOval.draw(win1)
oval = Oval(Point(20,200),Point(60,280))
oval.draw(win1)

poly = Polygon(Point(40,320),Point(80,360),Point(20,340))
poly.draw(win1)
labelPoly = Text(Point(250,340),'Polygon - (40,320),(80,360),(20,340) ')
labelPoly.draw(win1)
line1Poly = Line(Point(40,290),Point(40,320))
line1Poly.setFill('red')
line1Poly.setArrow('last')
line1Poly.draw(win1)


#This part just keeps the window open when not run from interactive shell
def main():
    coord=win1.getMouse()
    x=coord.getX()
    y=coord.getY()
    return x,y

main()

    
