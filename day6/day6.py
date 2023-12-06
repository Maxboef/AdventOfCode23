def read_input():
    with open("input.txt") as file:
        return (file.readlines())
    
timeArray = []
distanceArray = []

for line in read_input():
    splittedArray = line.split(" ")

    for idx, value in enumerate(splittedArray):
        if idx == 0 or value == '' or value == '\n':
             continue
        
        if('\n' in value):
             value = value[:2]

        if('Time:' in splittedArray):
            timeArray.append(value)
        else:
            distanceArray.append(value)

totalCorrectValues = []

for idx, game in enumerate(timeArray):
    winConditions = 0
    gameLength = int(game)
    winnableDistance = int(distanceArray[idx])
    
    for i in range(gameLength):
        speed = int(i)

        if((speed * (gameLength - i)) >= winnableDistance):
            winConditions += 1

    totalCorrectValues.append(winConditions)


print(totalCorrectValues)

