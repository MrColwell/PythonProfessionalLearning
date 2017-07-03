total = 0
n = 0
stop = 0
nextMark = input('Type in a mark: ')

while stop == 0:
    nextMark = eval(nextMark)
    total = total+nextMark
    n = n + 1
    nextMark = input('Hit enter to stop, or type in a mark: ')
    if nextMark == "":
        stop = 1

print("You entered", n, 'marks.  The average is:',total/n)

       
