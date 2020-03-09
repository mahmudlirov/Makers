"""You are given a string.
In the first line, print the third character of this string.
In the second line, print the second to last character of this string.
In the third line, print the first five characters of this string.
In the fourth line, print all but the last two characters of this string.
In the fifth line, print all the characters of this string with even indices
(На английском языке, чтобы Вы научились remember indexing starts at 0, so the characters are displayed starting with
the first).
In the sixth line, print all the characters of this string with odd indices
(На английском языке, чтобы Вы научились i.e. starting with the second character in the string).
In the seventh line, print all the characters of the string in reverse order.
In the eighth line, print every second character of the string in reverse order,
starting from the last one.
In the ninth line, print the length of the given string."""

String_1 = ('In the first line, print the third character of this string.')
print(String_1[3::])
String_2 = ('In the second line, print the second to last character of this string.')
print(String_2[2:0:-1])
String_3 = ('In the third line, print the first five characters of this string.')
print(String_3[0:5])
String_4 = ('In the fourth line, print all but the last two characters of this string.')
print(String_4[:-2:])
String_5 = 'In the fifth line, print all the characters of this string with even indices'
print(String_5[0::2])
String_6 = 'In the sixth line, print all the characters of this string with odd indices'
print(String_6[1::2])
String_7 = 'In the seventh line, print all the characters of the string in reverse order.'
print(String_7 [::-1])
String_8 = 'In the eighth line, print every second character of the string in reverse order, starting from the last one.'
print(String_8[:1:-1])
String_9 = ('In the ninth line, print the length of the given string.')
print(len(String_9))