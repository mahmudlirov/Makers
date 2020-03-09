"""N students take K apples and distribute them among each other evenly. The
remaining (На английском языке, чтобы Вы научились the undivisible) part remains in the basket. How many apples will
each single student get? How many apples will remain in the basket?
The program reads the numbers N and K. It should print the two answers for
the questions above. (На английском языке, чтобы Вы научились Each N student will take K apples, and remains X)"""

while True:
    print("How many apples and How many students took apples\n")
    apples = int(input('K basket apples: '))
    students = int(input('N students takes apples: '))
    K = apples // students
    print("In basket", K, "apples {0}. students {1}".format(apples, students))

