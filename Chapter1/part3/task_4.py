"""Напишите функцию которая будет определять
полигдром ли введенная строка. Если да 2 то печатать
“True”, если нет “False”."""
def Palindrome():
    palindrome = input("введите слово полиндроме: ")
    Count = len(palindrome)
    for i in range(Count//2):
        if palindrome[i] != palindrome[-1-i]:
            print("это не полиндром")
            break
        print("это полиндром!")        
    return 'good job'

print(Palindrome())