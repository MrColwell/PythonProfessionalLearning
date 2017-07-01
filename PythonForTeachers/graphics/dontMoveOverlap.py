#dontMoveOverlap.py
#A.Colwell (2014)
#Python 3.x
'''
Move a ball around an area and it will not move over other objects.
'''
#Modules to Import
from graphics2 import *
from time import sleep

#Initial values
move={'Up':(0,-2),'Down':(0,2),'Left':(-2,0),'Right':(2,0)}


win=GraphWin('Not going over an Obstacle',600,400)      #draw a canvas

topwall=Rectangle(Point(0,0),Point(600,5))
topwall.setFill('black')
topwall.draw(win)
botwall=Rectangle(Point(0,395),Point(600,400))
botwall.setFill('black')
botwall.draw(win)
leftwall=Rectangle(Point(0,5),Point(5,395))
leftwall.setFill('black')
leftwall.draw(win)
rightwall=Rectangle(Point(595,5),Point(600,395))
rightwall.setFill('black')
rightwall.draw(win)


box=Rectangle(Point(100,50),Point(150,150))         #draw obstacles
box.setFill('Maroon')
box.draw(win)

circle=Circle(Point(400,250),50)
circle.setFill('Maroon')
circle.draw(win)

player=Circle(Point(200,200),10)                    #draw player object
player.setFill('yellow')
player.draw(win)

title=Text(Point(400,100),'Use arrow keys to move.\nDelete wipes screen')
title.draw(win)

#Main Program
dx,dy=0,0
while win.isOpen() == True:

    k=win.checkKey()
    if k!='':
        if k == 'Delete':
            win.clear()

        elif k == 'q':
            win.close()
        else:
            pass
        try:
            dx,dy=move[k]
            #player.move(dx,dy)
            
                
        except:
            pass
    else:
        pass
    
    player.move(dx,dy)    
    o=player.getOverlap()                   #check for overlap
    if o==True:                             #move player back
        player.move(dx*-1,dy*-1)
    else:
        pass

    sleep(.01)
    

