l = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'f', 'a', 'b', 'c', 'd', 'f']

set(l)

print(list(set(l)))


x = set([1, 6, 7]) - set([1, 2, 3, 5])

print(x)

x = set('spam') - set(['h', 'a', 'm'])

print(x)

x = set(dir(bytearray)) - set(dir(bytes))

print(x)


l1, l2 = [1, 3, 4, 5, 2], [2, 3, 5, 4, 1]  # Order matters in sequence

print(l1 == l2)

l1, l2 = (1, 2, 3, 4, 5), (1, 2, 3, 4, 5)

print(l1 == l2)

x = set(l1) == set(l2)

print(x)

print(sorted(l1) == sorted(l2))


engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}

print(engineers & managers)

print(engineers - managers)

print(engineers > managers)  # Are engineers superset of managers

print(engineers < managers)  # Are engineers subset of managers

print((engineers & managers) > managers)

print((engineers | managers) > managers)  # All people is a superset of managers

print(engineers ^ managers)  # who is one but not both


