#changeText.py
#A.Colwell(2014)
'''
Program counts to 10 using a text box.
The numbers change almost every second.
'''
from graphics import *
from time import sleep

w=GraphWin('Changing Text',300,200)

text=Text(Point(150,106),'0')
text.draw(w)

for i in range(10):
    sleep(1)
    text.setText(str(i+1))
    if w.isOpen() == False:
        print('Counting stopped because you closed the window!')
        exit()
sleep(2)
w.close()
print('Finished counting.')



    


    
