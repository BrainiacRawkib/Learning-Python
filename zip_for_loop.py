a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 10)
c = [11, 12, 13, 14, 15]

x = zip(a, b, c)


# print(list(x))

for (x, y, z) in x:
    print(x, y, z, ' = ', x + y + z)

x = [1, 2, 3, 4]
y = [5, 6, 7]

z = zip(x, y)

print(list(z))


