# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

myList = [1, 2, 3, 5, 1, 5, 3, 10]
test = list(filter(lambda x: True if myList.count(x) == 1 else False, myList))
print(myList)
print(test)

