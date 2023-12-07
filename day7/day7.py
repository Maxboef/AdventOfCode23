from collections import Counter
import functools

lines = []

fiveOfAKind = []
fourOfAKind = []
fullHouse = []
threeOfAKind = []
twoPair = []
onePair = []
highCard = []
 

with open("input.txt") as file:
    lines = file.read().strip().split('\n')

for hand in lines:
    handCards = hand.split(' ')[0]

    maxValue = 0
    secondValue = 0
    jokers = 0

    dictionary = {}
    for card in handCards:
        dictionary[card] = dictionary.get(card, 0) + 1

    jokers = dictionary.get('J')
    if(jokers):
        dictionary.pop('J')
    
    if(dictionary):
        maxKey = max(dictionary, key=dictionary.get)
        maxValue = dictionary.get(maxKey)
        dictionary.pop(maxKey)

    if(jokers):
        maxValue += jokers

    if(dictionary):
        maxKey = max(dictionary, key=dictionary.get)
        secondValue = dictionary.get(maxKey)

    if(maxValue == 5):
        fiveOfAKind.append(hand)
    elif(maxValue == 4):
        fourOfAKind.append(hand)
    elif(maxValue == 3 and secondValue == 2):
        fullHouse.append(hand)
    elif(maxValue == 3):
        threeOfAKind.append(hand)
    elif(maxValue == 2 and secondValue == 2):
        twoPair.append(hand)
    elif(maxValue == 2):
        onePair.append(hand)
    else:
        highCard.append(hand)

sortOrder = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def value_sort(a, b):
    for idx, char in enumerate(a):
        aIndex = sortOrder.index(char)
        bIndex = sortOrder.index(b[idx])

        if(aIndex > bIndex):
            return -1
        if(aIndex == bIndex):
            continue
        else:
            return 1

fiveOfAKind = sorted(fiveOfAKind, key=functools.cmp_to_key(value_sort))
fourOfAKind = sorted(fourOfAKind, key=functools.cmp_to_key(value_sort))
fullHouse = sorted(fullHouse, key=functools.cmp_to_key(value_sort))
threeOfAKind = sorted(threeOfAKind, key=functools.cmp_to_key(value_sort))
twoPair = sorted(twoPair, key=functools.cmp_to_key(value_sort))
onePair = sorted(onePair, key=functools.cmp_to_key(value_sort))
highCard = sorted(highCard, key=functools.cmp_to_key(value_sort))

totalScore = 0
placementCounter = 1
mergedOrder = highCard + onePair + twoPair + threeOfAKind + fullHouse + fourOfAKind + fiveOfAKind

for hand in mergedOrder:
    totalScore += int(hand[6:]) * placementCounter
    placementCounter += 1

print(totalScore)
 