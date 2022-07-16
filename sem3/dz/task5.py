# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
    
checkInput = False
while not checkInput:
    try:
        n = int(input('Введите целое положительное число больше 0: '))
        checkInput = True if n > 0 else False 
    except:
        print('Введите  целое число корректно')
fibo = [0, 1]
negaFibo = [0, 1]
for index in range(0, n - 1):
    fibo.append(fibo[index] + fibo[index + 1])
    negaFibo.append(negaFibo[index] - negaFibo[index + 1])
negaFibo.reverse()
result = negaFibo + fibo[1:]
print(result)

    
    