from graphics import *
from time import sleep

#create a scary image for halloween
# we shall make a Jack'o'Lantern

win=GraphWin('Assignment 3 - Problem 3 - Scary Pumpkin',600,400)
win.setBackground('darkgrey')

pumpkin=Circle(Point(300,200),150)
pumpkin.setFill('orange')
pumpkin.draw(win)

leye=Polygon(Point(200,150),Point(250,150),Point(225,200))
leye.setFill('black')
leye.draw(win)

reye=Polygon(Point(400,150),Point(350,150),Point(375,200))
reye.setFill('black')
reye.draw(win)

mouth=Polygon(Point(225,250),Point(250,320), Point(300,275),Point(350,320),Point(375,250),Point(300,225))
mouth.setFill('black')
mouth.draw(win)

stem=Polygon(Point(300,20),Point(310,30),Point(320,60),Point(270,60),Point(300,40))
stem.setFill('green')
stem.draw(win)


for i in range(1000):
    stem.move(3,3)
    sleep(0.001)
    stem.move(-3,-3)
    sleep(0.001)
        
