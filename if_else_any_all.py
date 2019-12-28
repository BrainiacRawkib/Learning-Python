choice = 'ham'

d = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99, 'bacon': 1.10}

print(d[choice])

if None == False:
    print('This is True...')
else:
    print('This is False...')

x = 9

a = 'true' if x == 9 else 'false'

print(a)

a = 0

b = 0

c = 4

x = a or b or c or None

print(x)


l = ['love', 'hate', 8, 3, 4]

print(any(l))  # any works like or is equivalent to 'or' operator

l = []

print(any(l))

l = ['love', 'hate', 0, 3, 4, '']

print(all(l))  # all works like or is equivalent to 'and' operator

l = ['love', 'hate', 8, 3, 4]

print(all(l))  # all works like or is equivalent to 'and' operator



