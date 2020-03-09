"""Напишите функцию которая подсчитает количество
строк, слов и букв в текстовом файле."""

def String(stringCount):
    countWord = len(stringCount)
    countWords = stringCount.count(' ')
    countString = stringCount.count("\n")
    print(countWord, countWords, countString )
String("\n i'm so glad to see you here!!\n My name is Makhmud \n What about you? ")