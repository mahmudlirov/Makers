"""A timestamp is three numbers: a number of hours, minutes and seconds.
Given two timestamps, calculate how many seconds is between them. The
moment of the first timestamp occurred before the moment of the second
timestamp. (На английском языке, чтобы Вы научились 6, 1, 30, 6, 2, 10 result 40 sec.)"""


while True:
    hours1 = int(input("how many hours first?: "))
    minuts1 = int(input("how many minuts first?: "))
    sec_hours1 = hours1 * 3600
    sec_minut1 = minuts1 * 60
    count1 = sec_hours1 + sec_minut1
    hours2 = int(input("how many hours second?: "))
    minuts2 = int(input("how many minuts second?: "))
    sec_hours2 = hours2 * 3600
    sec_minut2 = minuts2 * 60
    count2 = sec_hours2 + sec_minut2
    difference = count1 - count2
    print("first time {0} second time {1} difference {2} sec".format(count1, count2, difference))