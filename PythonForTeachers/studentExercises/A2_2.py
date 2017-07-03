def acronym():
    stringVariable=input("Enter your phrase to turn into an acronym:")
    List1=stringVariable.split(" ")
    aList=[row[0] for row in List1]
    print(''.join(aList))

acronym()
