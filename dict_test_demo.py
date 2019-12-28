d = {'name': 'ade', 'age': 23, 'job': 'hacker'}

x = d.keys()

print(list(x))

x = d.get('post')

print(x)

x = d.get('post', 'M.D')

print(x)

d = {'name': 'ade', 'age': 23, 'job': 'hacker'}

print(d)

d2 = {'location': 'Nigeria', 'State': 'Lagos', 'job': 'Hacker dev'}

d.update(d2)

print(d)

table = {'Holy Grail': 1975, 'Life of Brian': 1979, 'The Meaning of Life': 1983, (): 'l', 1: 3}

print(list(table.items()))

x = [title for title, year in table.items() if year == 1975]

print(x)

matrix = {}

matrix[(2, 3, 4)] = 88

matrix[(7, 8, 9)] = 99

print(matrix)

if (2, 3, 6) in matrix:
    print(matrix[2, 3, 6])
else:
    print(0)


try:
    print(matrix[2, 3, 6])
except KeyError:
    print(0)

print(matrix.get((2, 3, 4), 0))

print(matrix.get((2, 3, 6), 0))

rec = {'name': 'Bob', 'jobs': ['developer', 'manager'], 'web': 'www.bobs.org/˜Bob',
       'home': {'state': 'Overworked', 'zip': 12345, 'Country': {'State': 'Las Vegas'}}}

print(rec['home']['Country']['State'])

db = ['1', 23, ('are', 23), ['wer', 34], {'a': 1, 'movie': 'Aquaman'}]

print(db[4]['movie'])

d = {}

d = d.fromkeys(['a', 'b'], 0)

print(d)

d = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}

print(d)

d = dict.fromkeys(['a', 'b', 'c'], 0)

print(d)

d = {k: 0 for k in ['a', 'b', 'c']}

print(d)

d = {}

d = d.fromkeys('spam')

print(d)

d = {'a': 1}

print(list(d.items()))

x = d.items() | d.keys() | {('c', 3), ('d', 4)}

print(x)

ks = d.keys()

print(sorted(ks))

d = {'b': 2, 'c': 3, 'a': 1, 'd': 4, 'e': 5}

for k in sorted(d):
    print(k, d[k])

print(d.get('f'))


if d.get('f') is not None:
    print('Present!', d['f'])
else:
    print('Missing Key!!!')









