p = (1, 2, 3, 4)

x, *y = p

print(x, y)


p = {'e': 0, 'f': 1, 'g': 2}

x, *y = p.items()

print('p.items(): ', x, y)

x, *y = p.keys()

print('p.keys(): ', x, y)

x, *y = p.fromkeys(y)

print('p.fromkeys(y): ', x, y)

x, *y = p.fromkeys(*y)

print('p.fromkeys(*y): ', x, *y)

x, *y = p.values()

print('p.values(): ', x, y)

x = p

print(x)

x = [1, 2, 'r', (4, 5, 6), 't']
print(type(x), x)
