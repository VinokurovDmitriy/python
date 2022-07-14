# Реализуйте алгоритм перемешивания списка
def getRandom(prevValue, maxValue):
    rand = random.randrange(0, maxValue)
    return rand if prevValue != rand else getRandom(rand, maxValue)
    

import random
newList = [2, 5, 7, 'u', '-', 't']
print(f'До перемешивания {newList}')
for i in range(0, len(newList)):
    newPosition = getRandom(0, len(newList))
    temp = newList[newPosition]
    newList[newPosition] = newList[i]
    newList[i] = temp
print(f'После смешивания {newList}')
    