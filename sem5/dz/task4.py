# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('data.txt', 'r') as fd:
    fdStr = fd.read()
rleData = ''
currentSymbol = fdStr[0]
count = 0
for index in range(1, len(fdStr)):
    count += 1
    if fdStr[index] != currentSymbol:
        currentSymbol = fdStr[index]
        rleData += str(count) + fdStr[index - 1]
        count = 1
    if index == len(fdStr) - 1:
        rleData += str(count) + fdStr[index - 1]
print('------------Шифрование------------')
print(fdStr)
print(rleData)
print('------------Дешифровка-------------')
with open('data2.txt', 'r') as fd2:
    fdStr2 = fd2.read()
rleData2 = ''
for index in range(1, len(fdStr2), 2):
    rleData2 += int(fdStr2[index - 1]) * fdStr2[index]
print(fdStr2)
print(rleData2)





