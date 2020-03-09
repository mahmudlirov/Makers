"""Given a string that may or may not contain a letter of interest. Print the
index location of the first and last appearance of f. If the letter f occurs
only once,then output its index. If the letter f does not occur, then do not
print anything.
Don't use loops in this task."""


string_with_f = 'I always wash my face in the morning and eat food'
print(string_with_f)
count_f = string_with_f.index("f")
count_last = string_with_f.rfind('f')
print("first f in {0} index, last f in {1} index".format(count_f, count_last))