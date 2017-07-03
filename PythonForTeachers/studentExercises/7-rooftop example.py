from graphics import *

win = GraphWin('Rooftop Triangle',600,400)

rooftop = Polygon(Point(300,100),Point(500,300),Point(100,300))
rooftop.setFill('blue')
rooftop.draw(win)
