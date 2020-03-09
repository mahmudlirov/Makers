"""Напишите функцию который будет конвертировать
Фаренгейт в Цельсии и наоборот."""
def FahrenheitAndCelsius():
    Fahrenheit = float(input("Enter your Fahrenheit: "))
    countFaToCe = (Fahrenheit  - 32) * 5/9
    print("Fahrenheit to Celsius: ",countFaToCe)
    Celsius = float(input("Enter your Celsius: "))
    countCeToFa = (Celsius * 5/9) + 32
    print("Celsius to Fahrenheit: ",countCeToFa)
    return 'Good job'
print(FahrenheitAndCelsius())

