#getText.py
#A.Colwell (2014)
#Python 3.x
'''
get  text from a text box, display in window
'''
#Modules to Import
from graphics import *
from time import sleep

#Initial values
window=GraphWin('Enter Text',400,300)

#Main Program
text=Entry(Point(200,150),20)
text.draw(window)
newText = Text(Point(200,70),'Text here')
newText.setTextColor('blue')
newText.draw(window)

while window.isOpen() == True:
    temp=text.getText()
    newText.setText(temp)

    

