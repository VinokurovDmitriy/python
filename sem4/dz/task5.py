# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
from getDegree import getDegree

def openFile(fileName):
    try:
        with open(fileName, 'r') as f:
            return f.read()
    except:
        print(f'Файл {fileName} не найден')
        return False
    
def parsePolynomial(strPol):
    coefDict = {}
    for item in strPol.split(' + '):
        degree = item.split('^')
        mult = item.split('*')
        if len(degree) > 1:
            key = degree[1]
            value = mult[0]
        elif len(mult) > 1:
            key = 1
            value = mult[0]
        else:
            key = 0
            value = item.replace(' = 0', '')
        coefDict[key] = value
    return coefDict

pol1 = parsePolynomial(openFile('task4.txt'))
pol2 = parsePolynomial(openFile('task5.txt'))
if(pol1 and pol2):
    if(len(pol1) > len(pol2)):
        firstPol = pol1
        secondPol = pol2
    else:
        firstPol = pol2
        secondPol = pol1
sumPolDict = {}
for key in firstPol.keys():
    sumPolDict[key] = int(firstPol[key]) + (int(secondPol[key] if key in secondPol else 0))
strPol = ''
with open('task5sum.txt', 'w') as f:
    for key in sumPolDict.keys():
        strPol += f'{sumPolDict[key]}{getDegree(int(key))}'
    f.write(strPol)
    
