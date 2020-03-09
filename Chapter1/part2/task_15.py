"""Write the code, which will print numbers from 0 till your age. And if your
age is odd, will be printed all odd numbers till your age, if even all even
numbers."""

while True:
    number = int(input("Enter your age: "))
    if number % 2 == 0:
        for num in range(0,number,2):
            print("Your age is even", num)
        print("Your age is even", number)
    elif number % 2 != 0:
        for num in range(1,number,2):
            print("Your age is odd", num)
        print("Your age is odd", number)
