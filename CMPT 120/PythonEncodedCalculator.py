#PythonEncodedCalculator
#My encoded calculator allows the user to input ANY length encoded equation as long as it follows the proper syntax noted in the program description when it is run. If a symbol does not match the ones used in this particular program, you will be notified to try again.
#Creator Jasper Quan (#301255149)
#Created June 16, 2017 : Last Edit June 18, 2017

import unicodedata
encodedList = ['$','&','@','?','!']
userOn = True #keeps track if the user wants to exit the program

#Make a function to calculate user input. Becomes a recursive function if user enters bad input.
def calc(string):
    badInput = False #keeps track if theres been bad input
    letterEntered = False #keeps track if a letter has been entered
    letter = 0
    result = 0
    checkList = string.split(' ')#convert string into lists, take out all the spaces
    resultList = []  
    noticePhrase = "\nYou have entered the equation '" + string + "' which is not a complete equation since it only contains the Please, try again." #allows me to create the same error message for similar failed inputs by the user
    noticeList = noticePhrase.split(' ')#allows me to modify the error message, fitting it to the specific error at hand
    
    for character in range(len(checkList)):#checks every character of the user input
        if character%2 == 0: #checks every character in an even index slot
            symbolCount = 0
            if checkList[character].upper() == 'X':#check if user wants to leave the program
                return(False)   
            else:
                if checkList[character] == ' ' or checkList[character] == '':#checks if user just hit enter
                    print('The equation you entered is \'' + string + "'")
                    print('\nHave you simply pressed the Enter key? Please, enter an equation next time! :)')
                    return(calc(intro()))      
                else:        
                    for count in range(len(encodedList)):#check if user input matches any symbol in my encoded list
                        if checkList[character] == encodedList[count]:
                            if badInput:
                                noticeList.insert(len(noticeList)-3,'and the')
                            else:
                                badInput = True
                            noticeList.insert(len(noticeList)-3,'operator')
                            noticeList.insert(len(noticeList)-3,checkList[character])
                        else:
                            symbolCount += 1
                    if checkList[character].isnumeric():
                        if badInput:
                            noticeList.insert(len(noticeList)-3,'and the')
                        else:
                            badInput = True
                        noticeList.insert(len(noticeList)-3,'operand')
                        noticeList.insert(len(noticeList)-3,checkList[character])
                        symbolCount = 0
                    else:
                        if symbolCount == 5:
                            if badInput:
                                noticeList.insert(len(noticeList)-3,'and the')
                            else:
                                badInput = True
                            noticeList.insert(len(noticeList)-3,'character')
                            noticeList.insert(len(noticeList)-3,checkList[character])

        if character%2 == 1 and checkList[character].isnumeric()==False:#check if odd indexes are symbols
            symbolCount = 0
            if len(checkList) >= 2 and checkList[0].isnumeric():
                if character != len(checkList)-1:
                    if checkList[character+1].isnumeric():
                        if result == 0:
                            result += int(checkList[0])
                        for symbol in range(len(encodedList)):#check if the input symbol matches any encoded symbols
                            if checkList[character] == encodedList[symbol]:
                                if symbol == 0:
                                    result += int(checkList[character+1])
                                else:
                                    if symbol == 1:
                                        result -= int(checkList[character+1])
                                    else:
                                        if symbol == 2:
                                            result *= int(checkList[character+1])
                                        else:
                                            if symbol == 3:
                                                result /= int(checkList[character+1])
                                            else:
                                                if symbol == 4:
                                                    result %= int(checkList[character+1])
                            else:
                                symbolCount += 1
                            if symbolCount == 5:#When all the symbols have been checked, and none match
                                if badInput:
                                    noticeList.insert(len(noticeList)-3,'and the')
                                else:
                                    badInput = True
                                noticeList.insert(len(noticeList)-3,'character')
                                noticeList.insert(len(noticeList)-3,checkList[character])
                                result = 0
                else:#if last input is a symbol, send to bad input 
                    result = 0
                        
        if character%2 == 1 and len(checkList) >= 2:
            if checkList[character].isnumeric():#if its a number in an odd slot and not a symbol
                if badInput:
                    noticeList.insert(len(noticeList)-3,'and the')
                else:
                    badInput = True
                noticeList.insert(len(noticeList)-3,'operand')
                noticeList.insert(len(noticeList)-3,checkList[character])
            else:
                if badInput:
                    noticeList.insert(len(noticeList)-3,'and the')
                else:
                    badInput = True
                for symbol in range(len(encodedList)): #check what the user input is in this slot index
                    if checkList[character] == encodedList[symbol]:
                        noticeList.insert(len(noticeList)-3,'operator')
                        noticeList.insert(len(noticeList)-3,checkList[character])
                    else:
                        letter += 1
                if letter == 5:
                    letterEntered = True
                if letterEntered:
                    noticeList.insert(len(noticeList)-3,'character')
                    noticeList.insert(len(noticeList)-3,checkList[character])
                letter = 0
                                 
    if symbolCount == 5:
        print('The equation you entered is \'' + string + '\'')
        print("\nYou have entered the sequence of letters '" + string +"' which is not an equation. Please, try again.")
        return(calc(intro()))
    else:
        if result == 0:
            noticeList[len(noticeList)-4] = noticeList[len(noticeList)-4] + '.'
            noticeList = ' '.join(noticeList)
            print('The equation you entered is \'' + string + '\'')
            print(noticeList)
            return(calc(intro()))
        
    resultList.append(string)
    resultList.append(round(result,4))
    return(resultList)

#Initializes the instructions as well as returns the user input>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def intro():
    print("""\nThis Python Encoded Calculator can
    \t add: use the Symbol $,
    \t subtract: use the symbol &,
    \t multiply: use the symbol @,
    \t divide: use the symbol ? (result is a float), and
    \t find the remainder: use the symbol !

The equation you enter must follow this syntax:
\t<operand><space><operator><space><operand>
As long as your equation follows this syntax, you can make it as long as you want!
An <operand> is any integer you wish.
A <space> is a white space character ;)""")
    userIn = input("Please, enter your equation or 'X' or 'x' to eXit the Calculator: ")
    return(userIn)

#Start of my program >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print('Welcome to my Python Encoded Calculator\n')      
while userOn:
    userIn = intro()
    if userIn.upper() == 'X':
        userOn = False
    else:
        Total = calc(userIn)
        if Total == False:
            userOn = False
        else:
            print("The equation you entered is '", Total[0] + "'.")
            print('\nThe equation is ' + Total[0] + ' = %g' %Total[1])    
print('Bye!')