s1 = 'abc'
s2 = 'xyz123'

x = map(ord, s1)

print(list(x))

keys = ['spam', 'eggs', 'toast']
values = [1, 2, 4]

d = dict(zip(keys, values))

print(d)

x = {k: v for k, v in zip(keys, values)}

print(x)



