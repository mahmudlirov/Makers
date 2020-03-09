"""Напишите функцию котрый будет определять
введенный год, высокосный или нет."""

def BiggestYear():
    EnterYear = int(input("Enter your year: "))
    if EnterYear > 2020:
        print("your year is higher than this year")
    elif EnterYear < 2020:
        print("your year is lower than this year")
    else: 
        return 'come on you can do more!!!'
        
print(BiggestYear())