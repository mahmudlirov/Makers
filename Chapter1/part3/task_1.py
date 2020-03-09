"""1.Напишите функцию которая будет суммировать
введенные три случайные цифры."""



def NumberCount():
    firstNumber = int(input("enter your fisrt number: "))
    secondNumber = int(input("enter your second number: "))
    thirdNumber = int(input("enter your third number: "))
    return firstNumber + secondNumber + thirdNumber

print(NumberCount())