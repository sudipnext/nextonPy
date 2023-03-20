import math
def FindCard(cards, currentCard):
    low, high = 0, len(cards)-1
    while (low <= high):
        midVal = math.ceil((low+high)/2)
        if (cards[midVal] == currentCard):
            return midVal
        elif (cards[midVal] > currentCard):
            low = midVal + 1
        elif (cards[midVal] < currentCard):
            high = midVal - 1
    return -1


print(FindCard([11, 9, 7, 6, 5, 4, 3, 2,  1], 3))
