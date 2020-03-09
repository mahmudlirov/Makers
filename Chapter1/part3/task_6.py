"""Напишите функцию которая подсчитает количество
счетных и несчетных чисел в списке чисел."""

"""def number(a,b):
    c = a - b
    if c % 2 == 0:
        print("even",c)
    elif c % 2 == 1:
        print("odd",c)
number(5,9)
"""

"""def PrintNumber(ListNumber):
    ListNumber = [1,2,3,4,5,6]
    for count in ListNumber:
        if count % 2 == 0:
            print("even",count)
        elif count % 2 == 1:
            print("odd",count)
        else:
            return 'it is not number'
#PrintNumber()
print(ListNumber)"""

def PrintNumber(listNumber):
    for count in listNumber:
        if count % 2 == 0:
            print("even", count)
        else:
            print("odd", count)
PrintNumber([1, 2, 3, 4, 5])