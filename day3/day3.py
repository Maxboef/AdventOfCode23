def read_input():
    with open("input.txt") as file:
        return (file.readlines())


schemaArray = []

validNumberArray = []

def format_schema_array():
    for i, schemaLine in enumerate(read_input()):
        schemaArray.append([])
    
        for j, schemaPosition in enumerate(schemaLine):
            if(schemaPosition != '\n'):
                schemaArray[i].append(schemaPosition)

    return schemaArray

def index_has_symbol_surroundings(i, j):
    #top
    foundSymbol = index_has_symbol(i, j - 1)
    # top right
    if not foundSymbol:
        foundSymbol = index_has_symbol(i + 1, j - 1)
    # right
    if not foundSymbol:
        foundSymbol = index_has_symbol(i + 1, j)
    # right bottom  
    if not foundSymbol:  
        foundSymbol = index_has_symbol(i + 1, j + 1)
    # bottom    
    if not foundSymbol:
        foundSymbol = index_has_symbol(i, j + 1)
    # bottom left 
    if not foundSymbol:    
        foundSymbol = index_has_symbol(i - 1, j + 1)
    # left     
    if not foundSymbol:
        foundSymbol = index_has_symbol(i - 1, j)
    # top left   
    if not foundSymbol:  
        foundSymbol = index_has_symbol(i - 1, j - 1)

    return foundSymbol

def index_has_gear_surroundings(i, j, currentNumber):
    #top
    if index_has_gear(i, j - 1):
        gearArray[i][j - 1].append(currentNumber)
    # top right
    if index_has_gear(i + 1, j - 1):
        gearArray[i + 1][j - 1].append(currentNumber)
    # right
    if index_has_gear(i + 1, j):
        gearArray[i + 1][j].append(currentNumber)
    # right bottom  
    if index_has_gear(i + 1, j + 1):
        gearArray[i + 1][j + 1].append(currentNumber)
    # bottom    
    if index_has_gear(i, j + 1):
        gearArray[i][j + 1].append(currentNumber)
    # bottom left 
    if index_has_gear(i - 1, j + 1):
        gearArray[i - 1][j + 1].append(currentNumber)
    # left     
    if index_has_gear(i - 1, j):
        gearArray[i - 1][j].append(currentNumber)
    # top left   
    if index_has_gear(i - 1, j - 1):
        gearArray[i - 1][j - 1].append(currentNumber)   

def index_has_symbol(i, j):
    if(i < 0 or i > len(schemaArray) - 1):
        return False
    
    if(j < 0 or j > len(schemaArray[i]) - 1):
        return False

    value = schemaArray[i][j]
    if(value.isnumeric() or value == '.'):
        return False

    return True

def index_has_gear(i, j):
    if(i < 0 or i > len(schemaArray) - 1):
        return False
    
    if(j < 0 or j > len(schemaArray[i]) - 1):
        return False

    value = schemaArray[i][j]
    if(value == '*'):
        return True

    return False


format_schema_array()
# Weird way to initialize multidimensional array. Because of pointers?
gearArray =  [[[] for i in range(len(schemaArray[0]))] for j in range(len(schemaArray))]

for i, line in enumerate(read_input()):
    currentNumber = ''

    for j, character in enumerate(line):
        if(character.isnumeric()):
            currentNumber += character
        elif(currentNumber != '' and (character.isnumeric() == False or j == len(line) - 1)):
            # Check if currentNumber is valid
            numberIsValid = False
            numberHasGear = False

            for idx, digit in enumerate(currentNumber):
                if not numberIsValid:
                    numberIsValid = index_has_symbol_surroundings(i, j - len(currentNumber) + idx)
                    index_has_gear_surroundings(i, j - len(currentNumber) + idx, currentNumber)
            
            if numberIsValid:
                validNumberArray.append(int(currentNumber))

            currentNumber = ''
        
sum = 0
for number in validNumberArray:
    sum += number


print(sum)

# check gearArray where value is 2
totalGearValue = 0

for i in gearArray:
    for j in i:
        if len(j) == 2:
            totalGearValue += int(j[0]) * int(j[1])

print(totalGearValue)