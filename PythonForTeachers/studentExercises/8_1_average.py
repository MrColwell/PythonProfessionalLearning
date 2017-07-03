marks = eval(input('How many marks to determine the average? '))

total = 0

for i in range(marks):
    x = eval(input('Enter the '+str(i+1)+' number: '))
    total = total + x

print('\nYour average mark is:', total/marks)
