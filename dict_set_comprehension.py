res = {}

for x in range(10):
    res[x] = x ** 3


print(res)


s = {x + y for x in 'abc' for y in 'def'}

print(s)

s = {x + y: (ord(x), ord(y)) for x in 'abc' for y in 'def'}

print(s)

z = {k: k.upper() * 2 for k in ['spam', 'ham', 'cam', 'tam'] if k[1] == 'a'}

print(z)


