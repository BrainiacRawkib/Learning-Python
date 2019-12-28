m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('item in row 2 column 3: ', m[1][2])

col1 = [row[0] for row in m]

print('items in column 1: ', col1)

col2 = [row[1] for row in m]

print('items in column 2: ', col2)

col3 = [row[2] for row in m]

print('items in column 3: ', col3)

add = [row[1] + 1 for row in m]
print(add)

row_filter = [row[1] for row in m if row[1] % 2 == 0]

print(row_filter)

diag_matrix = [m[i][i] for i in [0, 1, 2]]

print(diag_matrix)

i = [[x ** 2, x ** 3] for x in range(4)]

print(i)

i = [[x, x * 2, x / 2] for x in range(-6, 7, 2) if x > 0]

print(i)

i = (x for x in range(6))

print(list(i))

g = (sum(row) for row in m)

print(next(g))
print(next(g))
print(next(g))

y = list(map(sum, m))

print(y)


s = {sum(x) for x in m}

print(s)


x = {i: sum(m[i]) for i in range(3)}

print(x)

alphabets = '0123456789abcdefghijklmnopqrstuvwxyz'

y = {x: ord(x) for x in alphabets}

print(y)


s = (ord(x) for x in 'spamm')

print(list(s))

