#Drawing Viewer Application
#This program reads files containing coordinates, then draws symbols in those coordinates to show a picture
#Created by Jasper Quan
#Made: June 21, 2017

#clean up the file so everything is in a list
def file_cleaner(someFile):
    cleaned_list = []
    for line in someFile:
        cleaned_line = line.strip()
        cleaned_list.append(cleaned_line)
    return(cleaned_list)

def grid_layout(gridStructure, coordinates, symbol):
    gridList = gridStructure.split(' ')
    grid_column = int(gridList[0])
    grid_row = int(gridList[1])
    myGrid = [[' ' for aColumn in range(grid_column)]for aRow in range(grid_row)] 

#Where I insert the symbols at their coordinates
    for line in coordinates:
        line = line.split()
        row = int(line[0])
        column = int(line[1])
        myGrid[row][column] = symbol
    border = '-' * grid_column
    print('\n\n\n   ' + border)    
    draw(myGrid,grid_row)
    print('   ' + border) 
    return 
    
def draw(grid,numRows):
    for row in range(numRows):
        grid[row] = ''.join(grid[row])
        if row < 10:
            print('%i |'%row + grid[row] + '|')
        else:
            print('%i|'%row + grid[row] + '|')
    return

    

    


#Main Program#
user_online = True
print('''
***Welcome to my Drawing Viewer Application.***
This application displays a drawing stored in a text file!
''')

while user_online == True:
    userInput = input('Please, enter the path and name of your file containing a drawing OR X to exit: ')
    if userInput.upper() == 'X':
        user_online = False
    else:
        fileName = userInput 
        file = open(fileName, 'r')
        myList = file_cleaner(file)
        myGrid = grid_layout(myList[0],myList[2:],myList[1])
        file.close()