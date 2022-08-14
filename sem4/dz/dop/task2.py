# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

with open('task2.txt', 'r') as file:
    listNum = list(map(int, file.read().split(' ')))
for i in range(listNum[0], len(listNum)):
    if listNum[i] - 1 != listNum[i - 1]:
        print('Пропущенный элемент ', listNum[i] - 1)