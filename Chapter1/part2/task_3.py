"""Write a program that reads an integer number and prints its previous and
next numbers. See the examples below for the exact format your answers
should take. There shouldn't be a space before the period.
Remember that you can convert the numbers to strings using the function str.
(На английском языке, чтобы Вы научились The next number for the number 179 is 180. The previous number for the
number 179 is 178.)"""

while True:
    print("Hello i will prints its previous and next number")
    number = int(input("Enter your number: "))
    minus = number - 1
    plus = number + 1
    print("The next number for the number {0} is {2}. The previous number for the number {0} is {1}".format(number, minus, plus))
