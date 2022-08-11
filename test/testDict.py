myDict = {
    'one': '1',
    'two': '2',
    'three': '3'
}
newDict = dict(filter(lambda x: x[0] != 'three', myDict.items()))
print(newDict)