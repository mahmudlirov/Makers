"""A school decided to replace the desks in three classrooms. Each desk sits two
students. Given the number of students in each class, print the smallest
possible number of desks that can be purchased.
- The program should read three integers: the number of students in each of
the three classes, a, b and c respectively.
- In the first test there are three groups. The first group has 20 students and
thus needs 10 desks. The second group has 21 students, so they can get by
with no fewer than 11 desks. 11 desks is also enough for the third group of
22 students. So we need 32 desks in total."""


print("Hello could you enter your students")
while True:
    classroom_1 = int(input("Enter first classroom of students: "))
    classroom_2 = int(input("Enter second classroom of students: "))
    classroom_3 = int(input("Enter third classroom of students: "))

    first_class = classroom_1 // 2
    print("Desk in first classroom:", first_class)
    second_class = classroom_2 // 2
    print("Desk in second classroom:", second_class)
    third_class = classroom_3 // 2
    print("Desk in third classroom:", third_class)
    minimum = min(first_class, second_class, third_class)
    print("Minimum desk:", minimum)