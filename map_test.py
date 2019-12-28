m = map(lambda x: x ** 3, range(4))

# print(list(m))

print(m)

print(next(m))

print(next(m))

print(next(m))

print(next(m))


z = zip([1, 2, 3], [0, 9, 8])

print(z)

print(next(z))

print(next(z))

print(next(z))


m = map(abs, range(5))

# print(m)

print(next(m))

print(next(m))

print(next(m))

print(next(m))

print(next(m))


x = filter(bool, ['spam', '', 'ni'])

print(next(x))

print(next(x))


f = [x for x in ['spam', '', 'ni', 'foo'] if bool(x)]

print(f)

f = [x for x in ['spam', '', 'ni', 'foo'] if x]

print(f)



