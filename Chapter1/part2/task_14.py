Number = input("Enter your numbers: ")
even = 0
odd = 0
for x in Number:
    if int(x) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Evens numbers - {0}, and odds numbers - {1}".format(even,odd))