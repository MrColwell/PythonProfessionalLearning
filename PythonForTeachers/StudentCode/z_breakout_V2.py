#breakoutV2.py
#A. Colwell (2015)

# graphics2 module returns a TUPLE when using .getOverlap()
# The tuple will have two numbers, indicating which objects
# have overlapped. Only useful if you know the corresponding
# object. In this case, the first brick (brick1) is the first
# object drawn in the window, and therefore the object 1.
# All the bricks are drawn first, so their numbers are 1-36
# Paddle is number 37
# Ball is number 38

import math
import random
from graphics2 import *
from time import sleep, perf_counter

winx,winy=600,400
win = GraphWin('Brick Breaker',winx,winy)
win.setBackground('maroon')
move={'Left':(-4,0),'Right':(4,0),'':(0,0)}

# Angles used     |  Relative       |
#     270         |  Coordinates    |
#      |          | o---> positive  |
#  180-+-000      | |               |
#      |          | |  positive     |
#     090         | V               |


#ball movement variables
direction = 350
speed =600
accX = 0
accY = 600

#--------------------Bricks-----------------------------
bricksLeft = 36

brick1 = Rectangle(Point(0,40),Point(49,49))
brick1.setFill('grey')
brick1.setOutline('lightgrey')
brick1.draw(win)

brick2 = Rectangle(Point(50,40),Point(99,49))
brick2.setFill('grey')
brick2.setOutline('lightgrey')
brick2.draw(win)

brick3 = Rectangle(Point(100,40),Point(149,49))
brick3.setFill('grey')
brick3.setOutline('lightgrey')
brick3.draw(win)

brick4 = Rectangle(Point(150,40),Point(199,49))
brick4.setFill('grey')
brick4.setOutline('lightgrey')
brick4.draw(win)

brick5 = Rectangle(Point(200,40),Point(249,49))
brick5.setFill('grey')
brick5.setOutline('lightgrey')
brick5.draw(win)

brick6 = Rectangle(Point(250,40),Point(299,49))
brick6.setFill('grey')
brick6.setOutline('lightgrey')
brick6.draw(win)

brick7 = Rectangle(Point(300,40),Point(349,49))
brick7.setFill('grey')
brick7.setOutline('lightgrey')
brick7.draw(win)

brick8 = Rectangle(Point(350,40),Point(399,49))
brick8.setFill('grey')
brick8.setOutline('lightgrey')
brick8.draw(win)

brick9 = Rectangle(Point(400,40),Point(449,49))
brick9.setFill('grey')
brick9.setOutline('lightgrey')
brick9.draw(win)

brick10 = Rectangle(Point(450,40),Point(499,49))
brick10.setFill('grey')
brick10.setOutline('lightgrey')
brick10.draw(win)

brick11 = Rectangle(Point(500,40),Point(549,49))
brick11.setFill('grey')
brick11.setOutline('lightgrey')
brick11.draw(win)

brick12 = Rectangle(Point(550,40),Point(599,49))
brick12.setFill('grey')
brick12.setOutline('lightgrey')
brick12.draw(win)

brick13 = Rectangle(Point(0,30),Point(49,39))
brick13.setFill('grey')
brick13.setOutline('lightgrey')
brick13.draw(win)

brick14 = Rectangle(Point(50,30),Point(99,39))
brick14.setFill('grey')
brick14.setOutline('lightgrey')
brick14.draw(win)

brick15 = Rectangle(Point(100,30),Point(149,39))
brick15.setFill('grey')
brick15.setOutline('lightgrey')
brick15.draw(win)

brick16 = Rectangle(Point(150,30),Point(199,39))
brick16.setFill('grey')
brick16.setOutline('lightgrey')
brick16.draw(win)

brick17 = Rectangle(Point(200,30),Point(249,39))
brick17.setFill('grey')
brick17.setOutline('lightgrey')
brick17.draw(win)

brick18 = Rectangle(Point(250,30),Point(299,39))
brick18.setFill('grey')
brick18.setOutline('lightgrey')
brick18.draw(win)

brick19 = Rectangle(Point(300,30),Point(349,39))
brick19.setFill('grey')
brick19.setOutline('lightgrey')
brick19.draw(win)

brick20 = Rectangle(Point(350,30),Point(399,39))
brick20.setFill('grey')
brick20.setOutline('lightgrey')
brick20.draw(win)

brick21 = Rectangle(Point(400,30),Point(449,39))
brick21.setFill('grey')
brick21.setOutline('lightgrey')
brick21.draw(win)

brick22 = Rectangle(Point(450,30),Point(499,39))
brick22.setFill('grey')
brick22.setOutline('lightgrey')
brick22.draw(win)

brick23 = Rectangle(Point(500,30),Point(549,39))
brick23.setFill('grey')
brick23.setOutline('lightgrey')
brick23.draw(win)

brick24 = Rectangle(Point(550,30),Point(599,39))
brick24.setFill('grey')
brick24.setOutline('lightgrey')
brick24.draw(win)

brick25 = Rectangle(Point(0,20),Point(49,29))
brick25.setFill('grey')
brick25.setOutline('lightgrey')
brick25.draw(win)

brick26 = Rectangle(Point(50,20),Point(99,29))
brick26.setFill('grey')
brick26.setOutline('lightgrey')
brick26.draw(win)

brick27 = Rectangle(Point(100,20),Point(149,29))
brick27.setFill('grey')
brick27.setOutline('lightgrey')
brick27.draw(win)

brick28 = Rectangle(Point(150,20),Point(199,29))
brick28.setFill('grey')
brick28.setOutline('lightgrey')
brick28.draw(win)

brick29 = Rectangle(Point(200,20),Point(249,29))
brick29.setFill('grey')
brick29.setOutline('lightgrey')
brick29.draw(win)

brick30 = Rectangle(Point(250,20),Point(299,29))
brick30.setFill('grey')
brick30.setOutline('lightgrey')
brick30.draw(win)

brick31 = Rectangle(Point(300,20),Point(349,29))
brick31.setFill('grey')
brick31.setOutline('lightgrey')
brick31.draw(win)

brick32 = Rectangle(Point(350,20),Point(399,29))
brick32.setFill('grey')
brick32.setOutline('lightgrey')
brick32.draw(win)

brick33 = Rectangle(Point(400,20),Point(449,29))
brick33.setFill('grey')
brick33.setOutline('lightgrey')
brick33.draw(win)

brick34 = Rectangle(Point(450,20),Point(499,29))
brick34.setFill('grey')
brick34.setOutline('lightgrey')
brick34.draw(win)

brick35 = Rectangle(Point(500,20),Point(549,29))
brick35.setFill('grey')
brick35.setOutline('lightgrey')
brick35.draw(win)

brick36 = Rectangle(Point(550,20),Point(599,29))
brick36.setFill('grey')
brick36.setOutline('lightgrey')
brick36.draw(win)

#bricks 600/12=49 will be width of brick
#bricks        9 will be height of brick
#brickname will be based on 25-36  ************
#                           13-24  ************
#                            1-12  ************
#brickList is used to undraw the bricks in main program
#if a brick is hit, it is undrawn then a 0 is placed in the list
brickList=[[brick25,brick13,brick1],[brick26,brick14,brick2],
           [brick27,brick15,brick3],[brick28,brick16,brick4],
           [brick29,brick17,brick5],[brick30,brick18,brick6],
           [brick31,brick19,brick7],[brick32,brick20,brick8],
           [brick33,brick21,brick9],[brick34,brick22,brick10],
           [brick35,brick23,brick11],[brick36,brick24,brick12]]


#--------------------Paddle-----------------------------

px = winx/2-30
py = winy-30

paddle = Rectangle(Point(px,py),Point(px+60,py+10))
paddle.setFill('grey')
paddle.setOutline('black')
paddle.draw(win)

#--------------------Ball-------------------------------

bx = winx/2-5
by = winy/4-5
ball = Circle(Point(bx,by),5)
ball.setFill('yellow')
ball.setOutline('black')
ball.draw(win)

#--------------------Scoreboard-------------------------
score = 0
lives = 3
timer = 0
paddleHits = 0
sB = Text(Point(winx/2,winy/2),'Score:'+str(score)+'\nLives:'+str(lives))
sB.draw(win)
sB.setFill('lightgrey')



#--------------------Functions--------------------------

# controls movement physics for ball
def aVel(x,y,d,v,t,ax,ay):
    dr = math.radians(d)
    x2 = x+v*math.cos(dr)*t+0.5*ax*t*t
    y2 = y+v*math.sin(dr)*t+0.5*ay*t*t
    vx = v*(math.cos(dr))+ax*t
    vy = v*(math.sin(dr))+ay*t
    vt = math.sqrt(vx*vx+vy*vy)
    dt = math.degrees(math.atan2(vy,vx))
    return x2,y2,dt,vt

#--------------------Main Loop--------------------------
game = True                             #used in code to stop the game
startTime=time.perf_counter()
while win.isOpen() == True and game == True:
    
    #sleep(.005)                         # speed or slow the game
    t0=time.perf_counter()
    #look after the paddle
    m = win.checkKey()
    if m == 'Escape':
        win.close()
    else:
        try:
            x,y = move[m]
        except:
            pass
    paddle.move(x,y)
    c=paddle.getCenter()
    if c.getX() > (600-30):
        paddle.move(-1*(c.getX() - 570),0)
    if c.getX() < (0+30):
        paddle.move((-1*c.getX()+30),0)

    #look after ball movement

    
    dX,dY,direction,speed=aVel(bx,by,
                                  direction,
                                  speed,
                                  time.perf_counter()-t0,
                                  accX,accY)
    ball.move(int(round(dX))-int(round(bx)),int(round(dY))-int(round(by)))
    bx,by=dX,dY
    if int(round(by))>winy-5:
        direction = int(360 - direction)
        direction = direction + random.randint(1,91)-50
        lives = lives - 1
    elif int(round(bx))>winx-5:
        direction= int(180 - direction)
    elif int(round(by))<5:
        direction = int(360 - direction)
    elif int(round(bx))<5:
        direction= int(180 - direction)
    if direction > 360:
        direction = direction - 360
    elif direction < 1:
        direction = direction + 360



    #check for ball collisions
    bc = ball.getCenter()
    if bc.getY() < 50:                  #bricks collision section
        x=int(bc.getX()//50)            #convert width of window to x value (column)
        y=int(bc.getY()//10) - 2        #convert height of bricks area to y value (row)
        if brickList[x][y] != 0:        #check to see if brick has already been undrawn
            bricksLeft-=1
            score = score + 10
            if y==0:score+=20
            brickList[x][y].undraw()    #undraw brick
            brickList[x][y]=0           #replace brick object in list with number 0
            if direction > 180:
                direction= int(360 - direction)
            else:
                direction = int(180 - direction)


    if bc.getY() > 365:                 #out of bounds at bottom collision section
        if len(ball.getOverlap())>1:
            #compare ball center to paddle center
            difference = (bc.getX()-paddle.getCenter().getX())
            
            direction = int(360 - direction)+difference
            paddleHits += 1

        #elif bc.getY()>395:             #closes window if ball passes by paddle
        #    win.close()

    if direction > 360:
        direction = direction - 360
    elif direction < 1:
        direction = direction + 360
    if bricksLeft == 0:                # or lives == 0
        win.close()
    timer = round(time.perf_counter())
    
    timer = str(timer)
    sB.setText('Score:'+str(score)+
               '\nLives:'+str(lives)+
               '\nPaddle Hits:'+str(paddleHits)+
               '\nTime:'+timer)

totalTime=time.perf_counter()-startTime
print('\nTime:',round(totalTime,2),'seconds',
      '\nScore:',score,
      '\nPaddle Hits:',paddleHits,
      '\nTotal Score:',300+score-round(totalTime)+paddleHits,
      '\nGame has ended. Thanks for playing')
    
    

    
