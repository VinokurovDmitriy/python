from inputKeyboard import inputUser

# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def getSimpleMultiple(list, num, divisor):
    if num > 1:
        if num % divisor == 0: 
            list.append(divisor)
            num //= divisor
            divisor = 2
        else: divisor += 1   
        getSimpleMultiple(list, num, divisor)
        
n = inputUser()
listSimpleMultiple = []
getSimpleMultiple(listSimpleMultiple, n, 2)
print(listSimpleMultiple)

    
            
            
        