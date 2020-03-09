"""Напишите функцию где дан список целых чисел.
Заменить отрицательные на -1, положительные - на число
1, ноль оставить без изменений."""


"""def PrintNumber(listNumber):
    for cuont  in listNumber:
        if cuont > 0:
            print(1)
        elif cuont < 0:
            print(-1)
        else:
           print(0)
PrintNumber([-5,-4,-3,-2,-1,0,1,2,3,4,5,6])
"""

def changeNumbersInList(array: list):
    i = 0
    while i < len(array):
        if array[i] < 0:
            array[i] = -1
        elif array[i] > 0:
            array[i] = 1
        i += 1
    print(array)
changeNumbersInList([-5,-4,-3,-2,-1, 0, 1, 2, 3, 4, 5])