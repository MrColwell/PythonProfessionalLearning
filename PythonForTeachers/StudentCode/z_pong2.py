#pong.py
#A.Colwell (2014)
#Python 3.x
'''
A simple game of pong!
'''
#Modules to Import
from graphics import *
from time import sleep
from random import randrange

#Functions
def cenObj(obj):
    x=obj.getCenter().getX()
    y=obj.getCenter().getY()
    return x,y
def moveObj(obj,dx,dy):
    obj.move(dx,dy)
    return
#Initial values
#variables
wX,wY=600,400
pW=10
pH=80
won=0
resetServe=1
resetGame=1
cS=0
pS=0
bx=wX/2
by=wY/2
x=randrange(80,120)/100*randrange(-1,2,2)
y=randrange(80,120)/100*randrange(-1,2,2)
# setup window
w=GraphWin('Ping Pong Like Game', wX,wY)
w.setBackground('black')
cP=Rectangle(Point(20,wY/2-pH/2),Point(20+pW,wY/2+pH/2))
cP.setFill('white')
cP.draw(w)
pP=Rectangle(Point(wX-20,wY/2-pH/2),Point(wX-20-pW,wY/2+pH/2))
pP.setFill('white')
pP.draw(w)
ball=Circle(Point(bx,by),6)
ball.setFill('white')
ball.draw(w)
cSlabel=Text(Point(wX/4,10),cS)
cSlabel.setTextColor('white')
cSlabel.draw(w)
pSlabel=Text(Point(wX*3/4,10),pS)
pSlabel.setTextColor('white')
pSlabel.draw(w)
go=Text(Point(wX/2,wY*3/4),'Press a Key to Start\nFirst to 5 Wins!')
go.setTextColor('yellow')
winner=Text(Point(wX/2,wY/4),'Someone won?')
winner.setTextColor('green')
#Main Program
while w.isOpen() == True:                   
    sleep(.01)
    if resetGame == 1:
        bx,by=cenObj(ball)
        moveObj(ball,wX/2-bx,wY/2-by)        
        go.draw(w)
        if won >0:
            if won == 1:
                s='You Won! :)'
            elif won == 2:
                s='Computer Won! :('
            else:
                pass
            winner.setText(s)
            winner.draw(w)
        else:
            pass                  
        try:
            k=w.getKey()
        except:
            pass
        cS=0
        pS=0
        cSlabel.setText(str(cS))
        pSlabel.setText(str(pS))
        winner.undraw()
        go.undraw()
        sleep(.5)
    if resetServe == 1:
        x=randrange(80,120)/100*randrange(-1,2,2)
        y=randrange(80,120)/100*randrange(-1,2,2)
        bx,by=cenObj(ball)
        moveObj(ball,wX/2-bx,wY/2-by)       
    else:
        pass
    resetServe=0
    resetGame=0
    moveObj(ball,x,y)           #move ball
    bx,by= cenObj(ball)
    cx,cy=cenObj(cP)
    px,py=cenObj(pP)
    try:
        k=w.checkKey()              #Check for player move
        if k == 'Up':
            if py>pH/2:
                moveObj(pP,0,-3)
            else:
                pass
        elif k =='Down':
            if py<wY-(pH/2):                 
                moveObj(pP,0,3)
            else:
                pass
        else:
            pass
    except:
        pass
    if bx<wX/5:                 #Simple computer AI
                                #checks if the ball is on computer's side
        if by<cy:
            moveObj(cP,0,-1)
        elif by>cy:
            moveObj(cP,0,1)
        else:
            pass
    if by<3:                    #ball hit top wall?
        y*=-1                   #change dir
        moveObj(ball,x,y+(by-3))  #move back into area

    elif by>wY-3:               #ball hit bottom wall?
        y*=-1
        moveObj(ball,x,y-(by-wY+3))
    if bx>cx-pW/2 and bx<cx+pW/2 and by>cy-pH/2 and by<cy+pH/2:     #ball hit comp paddle?
        x*=-1
        y=y+(.01*abs(by-cy))
        moveObj(ball,x+(5-abs(cx-bx)),y)
    if bx>px-pW/2 and bx<px+pW/2 and by>py-pH/2 and by<py+pH/2:     #ball hit player paddle?
        x*=-1
        y=y+(.01*abs(by-cy))
        moveObj(ball,x-(5-abs(px-bx)),y)
    if bx<3:
        pS+=1
        pSlabel.setText(str(pS))
        if pS>4:
            resetGame=1
            won=1
        else:
            resetServe=1    
    elif bx>(wX-3):
        cS+=1
        cSlabel.setText(str(cS))
        if cS>4:
            resetGame=1
            won=2
        else:
            resetServe=1
    else:
        pass
    
    
       
       
       
    
