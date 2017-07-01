# 6_highScoreReader.py
# Andrew Colwell (July 2017)

def readHS():
    # returns playername, level, score
    # code depends on file in that format, one line per value
    fileName = r'highscore.txt'
    with open(fileName, 'r') as myFile:
        lineList = myFile.readlines()     # store all lines as list
    myFile.close()
    return lineList[0].strip(), int(lineList[1]),int(lineList[2])

def writeHS(name,level,score):
    # writes a file with three lines.
    # name argument is string, level is int, score is int
    fileName = r'highscore.txt'
    highscore = name+'\n'+str(level)+'\n'+str(score)+'\n'
    with open(fileName, 'w') as myFile:
        myFile.write(highscore)
    myFile.close()

if __name__ == '__main__':
    player, level, score = readHS()
    print('Player:',player)
    print('Level:',level)
    print('Score:',score)

    writeHS('Claire Voyant',10,1010)

        
