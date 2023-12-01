def read_input():
    with open("input.txt") as file:
        return (file.readlines())

numberArray = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
totalSum = 0

for coordString in read_input():
    coordValue = ''

    for character in coordString:
        if(character.isnumeric()):
            coordValue += character
    
    if(coordValue[0] and coordValue[len(coordValue) - 1]):
        totalString = coordValue[0]
        totalString += coordValue[len(coordValue) - 1]

        totalSum += int(totalString)
    

print(totalSum)
totalSum = 0

for coordString in read_input():
    firstValue = 0
    lastValue = 0
    currentString = ''

    # Find first char
    for character in coordString:
        currentString += character
        if(firstValue):
            break

    
        for idx, stringNumber in enumerate(numberArray):
            if(stringNumber in currentString):
                firstValue = idx + 1
                break
        
        if(character.isnumeric()):
            firstValue = int(character)

    currentString = ''

    for lastNumber in coordString[::-1]:
        currentString = lastNumber + currentString
        if(lastValue):
            break


        for idx, stringNumber in enumerate(numberArray):
            if(stringNumber in currentString):
                lastValue = idx + 1
        
        if(lastNumber.isnumeric()):
            lastValue = int(lastNumber)
            
        
    if(firstValue != 0 and lastValue != 0):
        total = str(firstValue) + str(lastValue);
        totalSum += int(total)

print(totalSum)
