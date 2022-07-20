def inputUser(text = None, typeInt = True):
    checkInput = False
    if not text:
        typeText = ('целое' if typeInt else 'вещественное') + ' число' 
    else: typeText = text
    while not checkInput:
        try:
            num = input(f'Введите {typeText} : ')
            n = int(num) if typeInt else float(num)
            checkInput = True if n > -1 else print('Сделайте корректный ввод')
        except:
            print()
            print(f'Введите {typeText} корректно')
    if checkInput:
                return n