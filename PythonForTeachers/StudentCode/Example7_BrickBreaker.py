#Breakout.py
#Author: QQQ
#C_Block

# graphics2 module returns a TUPLE when using .getOverlap(win)
# The tuple will have two numbers, indicating which objects
# have overlapped. Only useful if you know the corresponding
# object. In this case, the first brick (brick1) is the first
# object drawn in the window, and therefore the object 1.
# All the bricks are drawn first, so their numbers are 1-36
# Paddle is number 37
# Ball is number 38

# Submitting this document will give you 50% plus:
# 10% if you can add 10 points for every brick hit      yes
# 10% display points in the window                      yes
# 10% add 30 points for every brick in top row only     yes
# 10% vary direction of ball movement (any angle)
# 10% reset and replay game after finished              yes


from graphics2 import *
from time import sleep

playagain = 'y'

while playagain == 'y' or playagain =='yes':
    winx=600
    winy=400
    win = GraphWin('Brick Breaker',600,400)
    move={'Left':(-1,0),'Right':(1,0),'':(0,0)}
    speed = 30
    win.setBackground('black')
#--------------------Bricks-----------------------------
#--------------------Row 1------------------------------
    brick1 = Rectangle(Point(0,40),Point(49,49))
    brick1.setFill('lime')
    brick1.setOutline('black')
    brick1.draw(win)

    brick2 = Rectangle(Point(50,40),Point(99,49))
    brick2.setFill('lime')
    brick2.setOutline('black')
    brick2.draw(win)

    brick3 = Rectangle(Point(100,40),Point(149,49))
    brick3.setFill('lime')
    brick3.setOutline('black')
    brick3.draw(win)

    brick4 = Rectangle(Point(150,40),Point(199,49))
    brick4.setFill('lime')
    brick4.setOutline('black')
    brick4.draw(win)

    brick5 = Rectangle(Point(200,40),Point(249,49))
    brick5.setFill('lime')
    brick5.setOutline('black')
    brick5.draw(win)

    brick6 = Rectangle(Point(250,40),Point(299,49))
    brick6.setFill('lime')
    brick6.setOutline('black')
    brick6.draw(win)

    brick7 = Rectangle(Point(300,40),Point(349,49))
    brick7.setFill('lime')
    brick7.setOutline('black')
    brick7.draw(win)

    brick8 = Rectangle(Point(350,40),Point(399,49))
    brick8.setFill('lime')
    brick8.setOutline('black')
    brick8.draw(win)

    brick9 = Rectangle(Point(400,40),Point(449,49))
    brick9.setFill('lime')
    brick9.setOutline('black')
    brick9.draw(win)

    brick10 = Rectangle(Point(450,40),Point(499,49))
    brick10.setFill('lime')
    brick10.setOutline('black')
    brick10.draw(win)

    brick11 = Rectangle(Point(500,40),Point(549,49))
    brick11.setFill('lime')
    brick11.setOutline('black')
    brick11.draw(win)

    brick12 = Rectangle(Point(550,40),Point(599,49))
    brick12.setFill('lime')
    brick12.setOutline('black')
    brick12.draw(win)

#--------------------Row 2------------------------------

    brick13 = Rectangle(Point(0,30),Point(49,39))
    brick13.setFill('cyan')
    brick13.setOutline('black')
    brick13.draw(win)

    brick14 = Rectangle(Point(50,30),Point(99,39))
    brick14.setFill('cyan')
    brick14.setOutline('black')
    brick14.draw(win)

    brick15 = Rectangle(Point(100,30),Point(149,39))
    brick15.setFill('cyan')
    brick15.setOutline('black')
    brick15.draw(win)

    brick16 = Rectangle(Point(150,30),Point(199,39))
    brick16.setFill('cyan')
    brick16.setOutline('black')
    brick16.draw(win)

    brick17 = Rectangle(Point(200,30),Point(299,39))
    brick17.setFill('cyan')
    brick17.setOutline('black')
    brick17.draw(win)

    brick18 = Rectangle(Point(250,30),Point(299,39))
    brick18.setFill('cyan')
    brick18.setOutline('black')
    brick18.draw(win)

    brick19 = Rectangle(Point(300,30),Point(349,39))
    brick19.setFill('cyan')
    brick19.setOutline('black')
    brick19.draw(win)

    brick20 = Rectangle(Point(350,30),Point(399,39))
    brick20.setFill('cyan')
    brick20.setOutline('black')
    brick20.draw(win)

    brick21 = Rectangle(Point(400,30),Point(449,39))
    brick21.setFill('cyan')
    brick21.setOutline('black')
    brick21.draw(win)

    brick22 = Rectangle(Point(450,30),Point(499,39))
    brick22.setFill('cyan')
    brick22.setOutline('black')
    brick22.draw(win)

    brick23 = Rectangle(Point(500,30),Point(549,39))
    brick23.setFill('cyan')
    brick23.setOutline('black')
    brick23.draw(win)

    brick24 = Rectangle(Point(550,30),Point(599,39))
    brick24.setFill('cyan')
    brick24.setOutline('black')
    brick24.draw(win)

#--------------------Row 3------------------------------

    brick25 = Rectangle(Point(0,20),Point(49,29))
    brick25.setFill('red')
    brick25.setOutline('black')
    brick25.draw(win)

    brick26 = Rectangle(Point(50,20),Point(99,29))
    brick26.setFill('red')
    brick26.setOutline('black')
    brick26.draw(win)

    brick27 = Rectangle(Point(100,20),Point(149,29))
    brick27.setFill('red')
    brick27.setOutline('black')
    brick27.draw(win)

    brick28 = Rectangle(Point(150,20),Point(199,29))
    brick28.setFill('red')
    brick28.setOutline('black')
    brick28.draw(win)

    brick29 = Rectangle(Point(200,20),Point(249,29))
    brick29.setFill('red')
    brick29.setOutline('black')
    brick29.draw(win)

    brick30 = Rectangle(Point(250,20),Point(299,29))
    brick30.setFill('red')
    brick30.setOutline('black')
    brick30.draw(win)

    brick31 = Rectangle(Point(300,20),Point(349,29))
    brick31.setFill('red')
    brick31.setOutline('black')
    brick31.draw(win)

    brick32 = Rectangle(Point(350,20),Point(399,29))
    brick32.setFill('red')
    brick32.setOutline('black')
    brick32.draw(win)

    brick33 = Rectangle(Point(400,20),Point(449,29))
    brick33.setFill('red')
    brick33.setOutline('black')
    brick33.draw(win)

    brick34 = Rectangle(Point(450,20),Point(499,29))
    brick34.setFill('red')
    brick34.setOutline('black')
    brick34.draw(win)

    brick35 = Rectangle(Point(500,20),Point(549,29))
    brick35.setFill('red')
    brick35.setOutline('black')
    brick35.draw(win)

    brick36 = Rectangle(Point(550,20),Point(599,29))
    brick36.setFill('red')
    brick36.setOutline('black')
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
               [brick35,brick23,brick11],[brick24,brick24,brick12]]

#--------------------Paddle-----------------------------

    px = winx/2-30
    py = winy-30

    paddle = Rectangle(Point(px,py),Point(px+60,py+10))
    paddle.setFill('magenta2')
    paddle.setOutline('magenta2')
    paddle.draw(win)

#--------------------Ball-------------------------------

    bx = winx/2-5
    by = winy/4-5
    dx = 2
    dy = 2
    ball = Circle(Point(bx,by),5)
    ball.setFill('magenta2')
    ball.setOutline('magenta2')
    ball.draw(win)

#--------------------Functions--------------------------


#--------------------Main Loop--------------------------
    game = True                             #used in code to stop the game
    score = 0                               #score before starting the game
    scoretext = Text(Point(300,200),('Score:',str(score)))
    scoretext.draw(win)                     #Draws score in window
    scoretext.setFill('yellow')
    while win.isOpen() == True and game == True:
        sleep(0.005)                        # speed or slow the game
        #look after the paddle
        m = win.checkKey()
        if m == 'Escape':
            win.close()
        else:
            try:
                x,y = move[m]
            except:
                pass
        paddle.move(x*speed,y*speed)
        c=paddle.getCenter()
        if c.getX() > (600-30):
            paddle.move(-1*(c.getX() - 570),0)
        if c.getX() < (0+30):
            paddle.move((-1*c.getX()+30),0)

        #look after ball movement
        bc = ball.getCenter()
        if bc.getX() > 595:
            dx = dx*-1
            ball.move((bc.getX()-595)*-1,0)
        if bc.getX() < 5:
            dx = dx*-1
            ball.move((bc.getX()-5)*-1,0)
        if bc.getY() < 5:
            dy = dy*-1
            ball.move((bc.getY()-5)*-1,0)
        ball.move(dx,dy)

        #check for ball collisions
        if bc.getY() < 50:                  #bricks collision section
            x=int(bc.getX()//50)            #convert width of window to x value (column)
            y=int(bc.getY()//10) - 2        #convert height of bricks area to y value (row)
            if brickList[x][y] != 0 :       #check to see if brick has already been undrawn
                brickList[x][y].undraw()    #undraw brick
                brickList[x][y]=0           #replace brick object in list with number 0
                dy = dy*-1                  #change direction of ball movement
                ball.move(dx,dy+2)          #move ball with a nudge of 2 
                score = score + 10          #Adds 10 to score for every time there is a collision with a brick
                scoretext.setText('Score: ' + str(score))   #Sets the text for the score as the new score
                if bc.getY() <30:                  #If the ball hits the third row 20 additional points will be added to the score
                    score = score + 20
        #end game
        if bc.getY() > 365:                 #out of bounds at bottom collision section
            if len(ball.getOverlap())>1:
                dy*=-1
                ball.move(dx,dy-2)

            elif bc.getY()>395:             #closes window if ball passes by paddle
                win.close()
                print('Highscore:'(score))  #Displays highscore
        if score == 600:                    
            win.close()                     #If the highscore is reached then the window closes
            print('Highscore:'(score))      #Displays highscore
            print('Congratulations you won!') #Displays a winning message
    
    playagain = eval(input('Play again?'))  #Prompts user to choose if they want to play again

print('Brick Breakout has ended, thanks for playing.') #Message is displayed signifying the end of the game and highscore is displayed



    
