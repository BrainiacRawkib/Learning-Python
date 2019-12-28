x = set('spam')
y = {'h', 'a', 'm'}

print(type(x))

print(x, y)

print(x & y)

print(x | y)

print(x - y)

print(x > y)  # Superset

i = {n ** 2 for n in [1, 2, 3, 4]}

print(sorted(i))

print('p' in set('spam'))

i = {'s', 'p', 'a', 'm'}

print(i)

i.add('over')  # set .add() method takes only one argument not more than one

print(i)

i.add((1, 2, 4, 5))  # set .add() method cannot add list or dictionary because they are mutable(unhashable)

print(i)

i.add(3)

print(i)

x = (1, 2, 4, 5) in i

print(x)






