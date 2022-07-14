# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def checkPredicat(a, b, c):
    return not (x or y or z) == (not x and not y and not y)

rangeBool = [True, False]
result = 'Утверждение ложно'
for x in rangeBool:
    for y in rangeBool:
        for z in rangeBool:
            if checkPredicat(x, y, z):
                result = 'Утверждение истинно'
print(result)
                
