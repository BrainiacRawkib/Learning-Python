f = open('datafile.txt')

print(next(f))

print(f.__next__())

print(f.__next__())

L = [1, 2, 3]

i = iter(L)

print(i.__next__())

print(next(i))

print(i.__next__())

print('\n\n')

r = range(5)

x = iter(r)

print(x.__next__())

print(next(x))



