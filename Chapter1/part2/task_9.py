"""In mathematics, the factorial of an integer n, denoted by n! is the following
product:
n!=1×2×...×n
For the given integer n
calculate the value n!. Don't use math module in this exercise."""

"""factorial = int(input("Enter your factorial: "))
for n in range(factorial):
     factorial_n = factorial * n 
     print("your factril is", factorial_n)"""

factorial = int(input("Enter you factorial: "))

for n in range(1,factorial):
     
     f = n ** factorial
     
     print(f)
