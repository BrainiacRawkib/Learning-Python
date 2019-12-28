a, *b = 'spam'

print(a, b)

[spam, ham] = ['yum', 'YUM']

print(spam, ham)


[a, b, c] = [1, 2, 3]

print(a, b, c)


a, *b, c = 1, 2, 3, 4, 5, 6

print(a, b, c)

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

x, a = ['po', 'cl']
y = []

y[:] = 'open'

print(y)

# a[0] = 'ko'

print(x)

print(a)

x, a = [[], []]

a[:] = 'ko'
x[:] = 'close'

print(x)
print(a)


