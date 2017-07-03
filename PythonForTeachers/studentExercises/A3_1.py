from graphics import *

def main():
    win = GraphWin('Assignment3-1',400,400)
    face = Circle(Point(200,200),200)
    face.setFill('yellow')
    face.draw(win)
    leye = Circle(Point(200-80,200-50),50)
    leye.setFill('black')
    leye.draw(win)
    reye = Circle(Point(200+80,200-50),50)
    reye.setFill('black')
    reye.draw(win)
    #mouth will be 5 lines connected
    point1=Point(100,250)
    point2=Point(150,290)
    point3=Point(200,300)
    point4=Point(250,290)
    point5=Point(300,250)
    Line1=Line(point1,point2)
    Line2=Line(point2,point3)
    Line3=Line(point3,point4)
    Line4=Line(point4,point5)
    Line1.draw(win)
    Line2.draw(win)
    Line3.draw(win)
    Line4.draw(win)

main()
