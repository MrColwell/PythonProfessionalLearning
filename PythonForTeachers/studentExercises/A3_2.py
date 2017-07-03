from graphics import *

win=GraphWin('Assignment3-2: House',600,400)

#create the background
sky=Rectangle(Point(0,0),Point(599,259))
sky.setFill('blue')
sky.setOutline('blue')
ground=Rectangle(Point(0,260),Point(599,399))
ground.setFill('darkgreen')
ground.setOutline('darkgreen')
sky.draw(win)
ground.draw(win)

#create the sun
sun=Circle(Point(100,100),30)
sun.setFill('yellow')
sun.setOutline('yellow')
sun.draw(win)

#create sun rays
# numbers reference clock positions
ray0=Line(Point(100,40),Point(100,60)) #ray 20 px long
ray0.setFill('yellow')
ray0.draw(win)
ray6=Line(Point(100,140),Point(100,160)) #ray 10px from sun
ray6.setFill('yellow')
ray6.draw(win)
ray9=Line(Point(40,100),Point(60,100))
ray9.setFill('yellow')
ray9.draw(win)
ray3=Line(Point(140,100),Point(160,100))
ray3.setFill('yellow')
ray3.draw(win)
#ray10
ray10=Line(Point(58,58),Point(72,72))
ray10.setFill('yellow')
ray10.draw(win)
#ray2
ray2=Line(Point(128,72),Point(142,58))
ray2.setFill('yellow')
ray2.draw(win)
#ray4
ray4=Line(Point(128,128),Point(142,142))
ray4.setFill('yellow')
ray4.draw(win)
#ray8
ray8=Line(Point(58,142),Point(72,128))
ray8.setFill('yellow')
ray8.draw(win)

#Create the house
house=Rectangle(Point(400,300),Point(500,200))
house.setFill('brown')
house.setOutline('brown')
house.draw(win)

#create the roof
roof=Polygon(Point(400,200),Point(500,200),Point(450,175))
roof.setFill('black')
roof.draw(win)

#create the door
door=Rectangle(Point(465,300),Point(485,250))
door.setFill('black')
door.draw(win)

#create the window
window=Rectangle(Point(425,225),Point(450,250))
window.setFill('black')
window.draw(win)


