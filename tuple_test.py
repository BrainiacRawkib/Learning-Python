t = (1, 34, 0, 3, 5)

t = sorted(t)

print(t)

t = (1, 34, 0, 3, 5, ['wer', 'sew', 'moo'])

t[5][2] = 'toople'

print(t)

from collections import namedtuple


rec = namedtuple('profile', ['name', 'age', 'jobs'])
bob = rec(name='Bob', age=40.5, jobs=['dev', 'mgr'])

print(bob)

print(bob[0], bob[2])

print(bob.name, bob.jobs, bob.age)

x = namedtuple('location', ['country', 'state', 'zip_code'])

i = x(country='U.S', state='New Jersey', zip_code='11012')

print(i)

print(i.country, i.state, i.zip_code)

d = bob._asdict()

print(d['name'], d['jobs'])

print(d)

name, age, job = bob

print(name, age, job)

sob = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}

name, age, job = sob.values()

print(name, age, job)

for x in sob:
    print(sob[x])









