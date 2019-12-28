a = ['spam', 'maps']
b = a
b[0] = 'berry'
print(a)  # a prints ['berry', 'maps'] because a references the same on=bject as b, the update is reflected in a


a = ['spam']
b = a[:]  # this makes two copy of list so if a or b is changed, the other is not changed by indexing
b[0] = 'sugar'
print(a)  # a prints ['spam'] because the slice expression made a copy of the list object before it was assigned to b
# after the second assignment statement, there are two different list objects that have same value (in python, we say
# they are ==, but not 'is'). The third statement changes the value of the list object pointed to b, but not that of a.

print(b)

