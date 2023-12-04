def read_input():
    with open("input.txt") as file:
        return (file.readlines())

totalScore = 0
totalArray = []

for cardString in read_input():
    totalArray.append(1)


for idx, cardString in enumerate(read_input()):
    cardValue = 0
    cardWins = 0

    columnIndex = cardString.index(':')
    withoutGameId = (cardString[columnIndex+2:])

    winningString = withoutGameId.split(" | ")[0]
    ownString = withoutGameId.split(" | ")[1]

    winningNumbers = winningString.split(" ")
    ownNumbers = ownString.split(" ")

    for own in ownNumbers:
        own = own.strip()

        if (own in winningNumbers and own != ''):
            cardWins += 1
            if cardValue == 0:
                cardValue = 1
            else:
                cardValue = cardValue + cardValue
            
    for i in range(cardWins* totalArray[idx]):
        totalArray[idx + (i % cardWins ) + 1] += 1

    totalScore += cardValue

sum = 0

for i in totalArray:
    sum += int(i)

print(sum)
