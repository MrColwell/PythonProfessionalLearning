#breakout.py
#A. Colwell (2015)

# graphics2 module returns a TUPLE when using .getOverlap()
# The tuple will have two numbers, indicating which objects
# have overlapped. Only useful if you know the corresponding
# object. In this case, the first brick (brick1) is the first
# object drawn in the window, and therefore the object 1.
# All the bricks are drawn first, so their numbers are 1-36
# Paddle is number 37
# Ball is number 38

# Submitting this document will give you 50% plus:
# 10% if you can add 10 points for every brick hit   Yes
# 10% display points in the window                   Yes
# 10% add 30 points for every brick in top row only  No
# 10% vary direction of ball movement (any angle)    No
# 10% reset and replay game after finished           Yes
Power = 'On'
while Power == 'On':
    Reset = 'y'
    from graphics2 import *
    from time import sleep
    
    while Reset == 'y':
        winx=600
        winy=400
        win = GraphWin('Brick Breaker',600,400)
        move={'Left':(-1,0),'Right':(1,0),'':(0,0)}
        speed = 4
        #--------------------Start Game-----------------------------
        Start = Text(Point(300,200),'Click anywhere to start the game')
        Start.draw(win)
        coord=win.getMouse()
        x=coord.getX()
        y=coord.getY()
        if x<600 and y<400:
            Start.undraw()
            Esc = Text(Point(500,10),'Press Esc key to close the game')
            Esc.setSize(10)
            Esc.draw(win)
            
                #--------------------Bricks-----------------------------
            
            brick1 = Rectangle(Point(0,40),Point(49,49))
            brick1.setFill('red')
            brick1.setOutline('lightgrey')
            brick1.draw(win)

            brick2 = Rectangle(Point(50,40),Point(99,49))
            brick2.setFill('blue')
            brick2.setOutline('lightgrey')
            brick2.draw(win)

            brick3 = Rectangle(Point(100,40),Point(149,49))
            brick3.setFill('yellow')
            brick3.setOutline('lightgrey')
            brick3.draw(win)

            brick4 = Rectangle(Point(150,40),Point(199,49))
            brick4.setFill('green')
            brick4.setOutline('lightgrey')
            brick4.draw(win)

            brick5 = Rectangle(Point(200,40),Point(249,49))
            brick5.setFill('purple')
            brick5.setOutline('lightgrey')
            brick5.draw(win)

            brick6 = Rectangle(Point(250,40),Point(299,49))
            brick6.setFill('red')
            brick6.setOutline('lightgrey')
            brick6.draw(win)

            brick7 = Rectangle(Point(300,40),Point(349,49))
            brick7.setFill('blue')
            brick7.setOutline('lightgrey')
            brick7.draw(win)

            brick8 = Rectangle(Point(350,40),Point(399,49))
            brick8.setFill('green')
            brick8.setOutline('lightgrey')
            brick8.draw(win)

            brick9 = Rectangle(Point(400,40),Point(449,49))
            brick9.setFill('yellow')
            brick9.setOutline('lightgrey')
            brick9.draw(win)

            brick10 = Rectangle(Point(450,40),Point(499,49))
            brick10.setFill('purple')
            brick10.setOutline('lightgrey')
            brick10.draw(win)

            brick11 = Rectangle(Point(500,40),Point(549,49))
            brick11.setFill('red')
            brick11.setOutline('lightgrey')
            brick11.draw(win)

            brick12 = Rectangle(Point(550,40),Point(599,49))
            brick12.setFill('blue')
            brick12.setOutline('lightgrey')
            brick12.draw(win)

            brick13 = Rectangle(Point(0,30),Point(49,39))
            brick13.setFill('green')
            brick13.setOutline('lightgrey')
            brick13.draw(win)

            brick14 = Rectangle(Point(50,30),Point(99,39))
            brick14.setFill('yellow')
            brick14.setOutline('lightgrey')
            brick14.draw(win)

            brick15 = Rectangle(Point(100,30),Point(149,39))
            brick15.setFill('purple')
            brick15.setOutline('lightgrey')
            brick15.draw(win)

            brick16 = Rectangle(Point(150,30),Point(199,39))
            brick16.setFill('red')
            brick16.setOutline('lightgrey')
            brick16.draw(win)

            brick17 = Rectangle(Point(200,30),Point(299,39))
            brick17.setFill('blue')
            brick17.setOutline('lightgrey')
            brick17.draw(win)

            brick18 = Rectangle(Point(250,30),Point(299,39))
            brick18.setFill('green')
            brick18.setOutline('lightgrey')
            brick18.draw(win)

            brick19 = Rectangle(Point(300,30),Point(349,39))
            brick19.setFill('yellow')
            brick19.setOutline('lightgrey')
            brick19.draw(win)

            brick20 = Rectangle(Point(350,30),Point(399,39))
            brick20.setFill('purple')
            brick20.setOutline('lightgrey')
            brick20.draw(win)

            brick21 = Rectangle(Point(400,30),Point(449,39))
            brick21.setFill('red')
            brick21.setOutline('lightgrey')
            brick21.draw(win)

            brick22 = Rectangle(Point(450,30),Point(499,39))
            brick22.setFill('blue')
            brick22.setOutline('lightgrey')
            brick22.draw(win)

            brick23 = Rectangle(Point(500,30),Point(549,39))
            brick23.setFill('green')
            brick23.setOutline('lightgrey')
            brick23.draw(win)

            brick24 = Rectangle(Point(550,30),Point(599,39))
            brick24.setFill('yellow')
            brick24.setOutline('lightgrey')
            brick24.draw(win)

            brick25 = Rectangle(Point(0,20),Point(49,29))
            brick25.setFill('purple')
            brick25.setOutline('lightgrey')
            brick25.draw(win)

            brick26 = Rectangle(Point(50,20),Point(99,29))
            brick26.setFill('red')
            brick26.setOutline('lightgrey')
            brick26.draw(win)

            brick27 = Rectangle(Point(100,20),Point(149,29))
            brick27.setFill('blue')
            brick27.setOutline('lightgrey')
            brick27.draw(win)

            brick28 = Rectangle(Point(150,20),Point(199,29))
            brick28.setFill('green')
            brick28.setOutline('lightgrey')
            brick28.draw(win)

            brick29 = Rectangle(Point(200,20),Point(249,29))
            brick29.setFill('yellow')
            brick29.setOutline('lightgrey')
            brick29.draw(win)

            brick30 = Rectangle(Point(250,20),Point(299,29))
            brick30.setFill('purple')
            brick30.setOutline('lightgrey')
            brick30.draw(win)

            brick31 = Rectangle(Point(300,20),Point(349,29))
            brick31.setFill('red')
            brick31.setOutline('lightgrey')
            brick31.draw(win)

            brick32 = Rectangle(Point(350,20),Point(399,29))
            brick32.setFill('blue')
            brick32.setOutline('lightgrey')
            brick32.draw(win)

            brick33 = Rectangle(Point(400,20),Point(449,29))
            brick33.setFill('green')
            brick33.setOutline('lightgrey')
            brick33.draw(win)

            brick34 = Rectangle(Point(450,20),Point(499,29))
            brick34.setFill('yellow')
            brick34.setOutline('lightgrey')
            brick34.draw(win)

            brick35 = Rectangle(Point(500,20),Point(549,29))
            brick35.setFill('purple')
            brick35.setOutline('lightgrey')
            brick35.draw(win)

            brick36 = Rectangle(Point(550,20),Point(599,29))
            brick36.setFill('red')
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
            Reset = 'n'


        #--------------------Paddle-----------------------------

        px = winx/2-30
        py = winy-30

        paddle = Rectangle(Point(px,py),Point(px+60,py+10))
        paddle.setFill('black')
        paddle.setOutline('lightgrey')
        paddle.draw(win)

        #--------------------Ball-------------------------------

        bx = winx/2-5
        by = winy/4-5
        dx = 1
        dy = 1
        ball = Circle(Point(bx,by),5)
        ball.setFill('grey')
        ball.setOutline('black')
        ball.draw(win)

        #--------------------Functions--------------------------


        #--------------------Main Loop--------------------------
        score = 0
        scoreText = Text(Point(58,10),score)
        scoreText2 = Text(Point(24,10),'Score:')
        scoreText2.draw(win)

        game = True                             #used in code to stop the game

        while win.isOpen() == True and game == True:
            sleep(.005)                         # speed or slow the game

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
                    score = score+10
                    scoreText.undraw()
                    scoreText = Text(Point(58,10),score)
                    scoreText.draw(win)
                    dy = dy*-1                  #change direction of ball movement
                    ball.move(dx,dy+2)          #move ball with a nudge of 2 


            if bc.getY() > 365:                 #out of bounds at bottom collision section
                if len(ball.getOverlap())>1:
                    dy*=-1
                    ball.move(dx,dy-2)

                elif bc.getY()>395:             #closes window if ball passes by paddle
                    Replay = 'n'
                    win.close()
       #--------------------Retry--------------------------     
        win= GraphWin('Brick Breaker',600,400)

        label1 = Rectangle(Point(0,0),Point(300,405))
        label1.draw(win)
        label2 = Rectangle(Point(300,0),Point(600,405))
        label2.draw(win)
        label1.setFill('red')
        label2.setFill('blue')

        gameOver = Text(Point(300,20),'Game has ended. Your score was')
        gameOver.setSize(25)
        gameOver.draw(win)
        finalScore = Text(Point(300,50),score)
        finalScore.setSize(23)
        finalScore.draw(win)

        Retry = Text(Point(300,70),'Would you like to play again?')     
        Retry.setSize(15)
        Retry.draw(win)
        
        yes = Text(Point(150,200),'Yes')
        no = Text(Point(450,200),'No')
        yes.setSize(20)
        no.setSize(20)
        yes.draw(win)
        no.draw(win)

        coord=win.getMouse()
        x=coord.getX()
        y=coord.getY()
        if x<300 and y<400:
            Reset = 'y'
            win.close()
        if x>300 and y<400:
            Reset = 'n'
            win.close()
        if Reset == 'n':
            Power = 'Off'
#--------------------Final Message--------------------------
win= GraphWin('Brick Breaker',600,200)
win.setBackground('yellow')
End = Text(Point(300,100),'Thank You For Playing!!! :)')
End.draw(win)
End.setSize(36)
End.setTextColor('blue')
Closing = Text(Point(300,150),'Click anywhere to close')
Closing.draw(win)
coord=win.getMouse()
x=coord.getX()
y=coord.getY()
if x<600 and y<200:
    win.close()

    
    

    
