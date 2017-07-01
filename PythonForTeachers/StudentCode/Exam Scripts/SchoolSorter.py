#SchoolSorter.py
# A. Colwell (Jan 2016)

import os

def addDistrict(district,school):
    schools[district]=[school]
    return

def addSchool(district,school):
    temp = schools[district]
    temp.append(school)
    schools[district]=temp

schools={}  #District:Schools List

try:
    schoolFile = open(r'Q:\CS110\NBSchools.txt', mode = 'r')
except:
    print('Could not read file!')

nextSchool = schoolFile.readline()
nextSchool = nextSchool.strip()

while nextSchool != '':
    tempList = nextSchool.split('\t')
    #print(tempList)
    if tempList[1] in schools.keys():
        #print(tempList[1])
        addSchool(tempList[1],tempList[0])
        
    else:
        #print(tempList[0])
        addDistrict(tempList[1],tempList[0])

    nextSchool = schoolFile.readline()
    nextSchool = nextSchool.strip()
   
schoolFile.close()

goOn = 'y'
while goOn == 'y':
    print('Which district would you like to have a list of schools?')
    count = 0
    schoolz = list(schools.keys())
    schoolz.sort()
    for item in schoolz:
        print(item)   

    userInput = input('Type in district from list above:')
    try:
        x=schools[userInput]
        for item in x:
            print(item)
            count+=1
        print('There are',count,'schools in that district')

    except:
        print('Sorry, no district with that name.')

    goOn = input('Again? (y/n)')
