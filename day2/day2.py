def read_input():
    with open("input.txt") as file:
        return (file.readlines())

totalGameId = 0
totalGamescore = 0

totalRed = 12
totalGreen = 13
totalBlue = 14

def find_game_id(gamestring):
    numberString = ''
    columnIndex = gamestring.index(':')
    numberString += gamestring[5]

    if(columnIndex == 7):
        numberString += gamestring[6]

    if(columnIndex == 8):
        numberString += gamestring[7]

    return numberString

def check_valid_game(gamestring):
    startIndex = gamestring.index(':')
    withoutGameId = (gamestring[startIndex+2:])

    splittedGames = withoutGameId.split(";")
    for game in splittedGames:
        for color in game.split(","):
            gameRedCounter = return_amount_of_color(color, 'red')
            gameGreenCounter = return_amount_of_color(color, 'green')
            gameBlueCounter = return_amount_of_color(color, 'blue')

            if(gameRedCounter > totalRed or gameGreenCounter > totalGreen or gameBlueCounter > totalBlue):
                return False
            
    return True

def return_amount_of_color(color, findString):
    if(findString in color):
        returnString = ''

        if(color[0].isnumeric()):
            returnString += color[0]

        if(color[1].isnumeric()):
            returnString += color[1]
        
        if(color[2].isnumeric()):
            returnString += color[2]

        return int(returnString)
    else:
        return 0
    
def get_total_game_score(gamestring):
    startIndex = gamestring.index(':')
    withoutGameId = (gamestring[startIndex+2:])

    maxRed = 1
    maxGreen = 1
    maxBlue = 1

    splittedGames = withoutGameId.split(";")
    for game in splittedGames:
        for color in game.split(","):
            totalRed = return_amount_of_color(color, 'red')
            totalGreen = return_amount_of_color(color, 'green')
            totalBlue = return_amount_of_color(color, 'blue')

            if(totalRed > maxRed):
                maxRed = totalRed
                
            if(totalGreen > maxGreen):
                maxGreen = totalGreen

            if(totalBlue > maxBlue):
                maxBlue = totalBlue

    return maxRed * maxGreen * maxBlue

for gameString in read_input():

    if(check_valid_game(gameString)):
        totalGameId += int(find_game_id(gameString))

    totalGamescore += int(get_total_game_score(gameString))

print (totalGameId)
print (totalGamescore)



