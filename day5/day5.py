def read_input():
    with open("input.txt") as file:
        return (file.readlines())

seeds = read_input()[0].split(' ')[1:]
seedMap = []
for val in seeds:
    if('\n' in val):
        val = val[:2]

    seedMap.append(int(val))


newSeedmap = []
for idx, value in enumerate(seedMap):
    newValue = 0
    if(idx % 2 != 0):
        newSeedmap.append(newValue + i)
    else:
        newValue = value
            
print(newSeedmap)


soilMap = [] 
fertilizerMap = [] 
waterMap = []
lightMap = []
temperatureMap = []
humidityMap = []
locationMap = []

# print(seedMap)

#FormatArrays
latestMap = seedMap.copy()
currentMap = latestMap.copy()

for line in read_input():
    if("to-fertilizer" in line):
        soilMap = latestMap.copy()
        currentMap = latestMap.copy()

    elif("to-water" in line):
        fertilizerMap = latestMap.copy()
        currentMap = latestMap.copy()

    elif("to-light" in line):
        waterMap = latestMap.copy()
        currentMap = latestMap.copy()

    elif("to-temperature" in line):
        lightMap = latestMap.copy() 
        currentMap = latestMap.copy()

    elif("to-humidity" in line):
        temperatureMap = latestMap.copy()
        currentMap = latestMap.copy()

    elif("to-location" in line):
        humidityMap = latestMap.copy()
        currentMap = latestMap.copy()

    elif(len(line.split(' ')) == 3):
        values = line.split(' ')

        destValue = int(values[0])
        seedValue = int(values[1])
        length = int(values[2])

        for idx, value in enumerate(currentMap):
            if(value >= seedValue and value < seedValue + length):
                newValue = (value - seedValue) + destValue 
                latestMap[idx] = newValue

locationMap = latestMap.copy()


# print(soilMap)    
# print(fertilizerMap)
# print(waterMap)
# print(lightMap)
# print(temperatureMap)
# print(humidityMap)
# print(locationMap)

# print(min(locationMap))