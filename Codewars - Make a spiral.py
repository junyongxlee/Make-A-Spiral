# Asks for user to input an integer to determine the size of spiral
inputValue = None
while True:
    try:
        inputValue = int(input('Enter an integer larger than 4 for the size of spiral: '))
        if(inputValue<5):
            print('Please enter an integer larger than 4 \n')
            continue
    except ValueError:
        print('Please enter a valid integer \n')
        continue
    break

print("\nPrinting a spiral with the size of " + str(inputValue) + "x" + str(inputValue) + "\n")
    
# Initialize a 2d array with user input size, then start with top left being a 1, and direction moving to the right
map = [ [0] * inputValue for _ in range(inputValue)]
map[0][0] = 1

currentX = 0
currentY = 0
direction = 'R'

# Function for going left
def goLeft():
    global currentX, currentY, map, direction
    
    # If left is a wall then change direction
    if(currentX-1 < 0):
        direction = 'U'
    # If left side had already been 'walked' on, it means we're going backwards so we should stop walking
    elif(map[currentY][currentX-1] == 1):
        direction = 'STOP'
    # If 2 blocks to the left is a wall and there is no block on top, then walk left
    elif(currentX - 2 == -1 and map[currentY-1][currentX-1] != 1):
        currentX -=1
        map[currentY][currentX] = 1
    # If 2 blocks to the left is empty and there is no block on top, then walk left
    elif(map[currentY][currentX-2] != 1 and map[currentY-1][currentX-1] != 1):
        currentX -=1
        map[currentY][currentX] = 1
    # No move could be done so we're changing directions
    else:
        direction = 'U'

# Function for going right
def goRight():
    global currentX, currentY, map, direction
    
    # Checks if right is a wall, if yes then change direction
    if(currentX+1 == inputValue):
        direction = 'D'
    # If the right side has been 'walked' on, it means we're going backwards so we should stop walking
    elif(map[currentY][currentX+1] == 1):
        direction = 'STOP'
    # If 2 blocks to the right is a wall and there is no block on bottom, then walk left
    elif(currentX + 2 == inputValue and map[currentY+1][currentX+1] != 1):
        currentX +=1
        map[currentY][currentX] = 1
    # If 2 blocks to the right is empty and there is no block on bottom, then walk left
    elif(map[currentY][currentX+2] != 1 and map[currentY+1][currentX+1] != 1):
        currentX +=1
        map[currentY][currentX] = 1
    # No move could be done so we're changing directions
    else:
        direction = 'D'
        
# Function for going down
def goDown():
    global currentX, currentY, map, direction
    # Checks if bottom is a wall, if yes then change direction
    if(currentY+1 == inputValue):
        direction = 'L'
    # If the bottom side has been 'walked' on, it means we're going backwards so we should stop walking
    elif(map[currentY+1][currentX] == 1):
        direction = 'STOP'
    # If 2 blocks to the bottom is a wall and there is no block on left, then walk dowm
    elif(currentY + 2 == inputValue and map[currentY+1][currentX-1] != 1):
        currentY +=1
        map[currentY][currentX] = 1
    # If 2 blocks to the bottom is empty and there is no block on left, then walk down
    elif(map[currentY+2][currentX] != 1 and map[currentY+1][currentX-1] != 1):
        currentY +=1
        map[currentY][currentX] = 1
    # No move could be done so we're changing directions
    else:
        direction = 'L'

# Function for going up
def goUp():
    global currentX, currentY, map, direction
    
    # Checks if top is a wall, if yes then change direction
    if(currentY-1 < 0):
        direction = 'R'
    # If the top side has been 'walked' on, it means we're going backwards so we should stop walking
    if(map[currentY-1][currentX] == 1):
        direction = 'STOP'
    # If 2 blocks to the top is a wall and there is no block on right, then walk up    
    elif(currentY - 2 == -1 and map[currentY-1][currentX+1] != 1):
        currentY -=1
        map[currentY][currentX] = 1
    # If 2 blocks to the top is empty and there is no block on right, then walk down
    elif(map[currentY-2][currentX] != 1 and map[currentY-1][currentX+1] != 1):
        currentY -=1
        map[currentY][currentX] = 1
    # No move could be done so we're changing directions
    else:
        direction = 'R'

# Loop to keep moving until STOP is returned
while True:
    if direction == 'STOP':
        break
            
    if direction == 'R':
        goRight()
        
    elif direction == 'D':
        goDown()
        
    elif direction == 'L':
        goLeft()
        
    elif direction == 'U':
        goUp()

# Prints a spiral based on the map array values
for j in range(inputValue):
    for i in range(inputValue):
        if(map[j][i] == 1):
            print ('0', end = '')
        else:
            print('.', end = '')
    print()
    
input("\n\nPress enter to quit :)")
