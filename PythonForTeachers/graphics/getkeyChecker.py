#changeText.py
#A.Colwell(2014)
#Python 3.x

from graphics import *
'''
Examples of other keys:
Control_L, Shift_L, Caps_Lock, Caps_Lock, quoteleft, comma, period
slash, semicolon, quoteright, bracketleft, bracketright, backslash
Delete, Insert, Home, End, Next, Prior, slash, asterisk, minus, plus
Return, Left, Right, Down, Up, Escape

'''

w=GraphWin('getKey() Test',600,400)

stop =0
while stop == 0:
    s=w.getKey()
    print(s)

    if s == 'Escape':
        stop = 1


