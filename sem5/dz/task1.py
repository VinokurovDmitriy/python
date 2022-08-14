# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'абвгдейка, абвгдейка —Это учёба и игра, абвгдейка, абвгдейка,'
newString = ''
newString = list(filter(lambda word: 'абв' not in word, text.split(' ')))
print('было: ', text)
print('стало: ', ' '.join(newString))