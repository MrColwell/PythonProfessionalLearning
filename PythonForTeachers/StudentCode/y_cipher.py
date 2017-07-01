def cipher():
    #this encodes just one single letter
    #store the alphabet as a string
    alphabet ='abcdefghijklmnopqrstuvwxyz'
    #get the letter from the user as a string
    original = input("What is the letter in to encode: ")
    #get the amount of shift from user as a number
    shift = eval(input("What is the shift value:"))
    #the new position of the letter will be the position plus shift
    number = alphabet.find(original) + shift
    #print out the new letter with the new position from the alphabet
    print('Encoded letter is:', alphabet[number])

def cipher2():
    #this encodes phrases, but space is part of the encoding
    alphabet ='abcdefghijklmnopqrstuvwxyz '
    original = input("What is the phrase to encode: ")
    original = original.lower()
    shift = eval(input("What is the shift value:"))
    phrase = list(original)
    numberized = [[x,alphabet.find(x)+shift] for x in phrase]
    encoded = [x[1] for x in numberized]
    converted = [[x,alphabet[x]] for x in encoded]
    convert1= [x[1] for x in converted]
    print('Original:',original,'\n',
          'phrase:',phrase,"\n",
          'numberized:',numberized,'\n',
          'encoded:',encoded,'\n',
          'converted:',converted,'\n',
          'convert1:',convert1,'\n',
          'Encoded phrase is:',"".join(convert1))
             

def cipher3():
    #this encodes just one single word alternate method
    #best conversion so far as it deals with the space
    alphabet ='abcdefghijklmnopqrstuvwxyz'
    original = input("What is the phrase to encode: ")
    original = original.lower()
    shift = eval(input("What is the shift value:"))
    shift = shift%26
    alphabet1=alphabet[:shift]
    alphabet2=alphabet[shift:]
    alphabet3=alphabet2+alphabet1+" !?<>@#$%^&*()+_-=[]{}\|`~.,"
    alphabet = alphabet+" !?<>@#$%^&*()+_-=[]{}\|`~.,"
    phrase = list(original)
    numberized =[alphabet.find(x) for x in phrase]
    encoded = [alphabet3[x] for x in numberized] 
    print('Original:',original,'\n',
          'phrase:',phrase,"\n",
          'numberized:',numberized,'\n',
          'encoded:', encoded,'\n',
          'Encoded phrase:',"".join(encoded))
    print('Encoded phrase:',"".join(encoded))

def cipher4():
    #this encodes phrase using dictionaries instead of strings and lists
    alpha2num = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,
                'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,
                'm':12,'n':13,'o':14,'p':15,'q':16,
                'r':17,'s':18,'t':19,'u':20,'v':21,
                'w':22,'x':23,'y':24,'z':25,' ':26}
    num2alpha = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',
                6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',
                12:'m',13:'n',14:'o',15:'p',16:'q',
                17:'r',18:'s',19:'t',20:'u',21:'v',
                22:'w',23:'x',24:'y',25:'z',26:' '}
    original = input("Enter your phrase to be encoded: ")
    original = original.lower()
    shift = eval(input("What is the shift value:"))
    phraseList = list(original)
    number = [alpha2num[x] for x in phraseList]
    number1 = [(x+shift)%27 for x in number]
    encoded = [num2alpha[x] for x in number1]
    print('original:',original,'\n',
          'shift:',shift,'\n',
          'phraseList:',phraseList,'\n',
          'number:',number,'\n',
          'number1:',number1,'\n',
          'encoded:',encoded,'\n',
          'Encoded phrase:',"".join(encoded))
    
    
      
          
cipher3()


    
