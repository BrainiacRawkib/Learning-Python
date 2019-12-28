a = ['wer', 'sew', 'rew']
b = a
c = b
c[0] = 'meing'
c[2] = 'moo'

print(a)

print(b)


x = [1, 2, 3]
l = ['a', x, 'b']
d = {'x': x, 'y': 2}

print(l)

print(d)

x[1] = 'surprise'

print(l)

print(d)

d['x'][2] = 'changed'

print(l)

print(d)

x = [1, 2, 3]
y = {'a': 1, 'b': 2}

a = x[:]
b = y.copy()

a[1] = 'newt'
b['c'] = 'spam'

print(a)

print(b)

x = [1, 2, 3]
l = ['a', x[:], 'b']
d = {'x': x[:], 'y': 2}

l[1][2] = 'list change'
d['x'][2] = 'dict change'

print(x)
print(l)
print(d, '\n')


a = [1, {'a': 1, 'b': {'loop': 'for', 'condition': 'if-else'}}, 3]
b = ['a', a[:], 'b']
c = {'x': a[:], 'y': 2}


# b[1][1] = 'list change'
# c['x'][1] = 'dict change'


print(a)
print(b)
print(c)

l1 = '(1, (2, 3))'

l2 = '(1, (2, 3))'

print(l1 == l2, l1 is l2)
print(id(l1), id(l2))

l1 = (1, (2, 3))

l2 = (1, (2, 3))

print(l1 == l2, l1 is l2)
print(id(l1), id(l2))


l1 = 'a longer string'

l2 = 'a longer string'

print(l1 == l2, l1 is l2)
print(id(l1), id(l2))


print(isinstance(1, int))

l = [4, 5, 6]

x = l * 4

y = [l] * 4

l[1] = 0  # impacts y but not x

print(x)

print(l)

print(y)

l = [4, 5, 6]
y = [list(l) for i in range(4)]

y[0][1] = 99

print(y)

l = [34, 'wer']

l = ['grail']

l.append(l)  # cyclic data structures

print(l)

x = {'a', 'd', 3}

y = x.copy()

print(y)

x = ['q', 'we', 3, 'g', 5, 6]

print(x[3:])




