import sys

print(len(dir(sys)))

x = len([x for x in dir(sys) if x.startswith('__')])

print(x)

y = len([y for y in dir(sys) if not y.startswith('__')])

print(y)

print(dir([]))

print(dir(''))


def dir1(x):
    return x, [a for a in dir(x) if not a.startswith('__')]


print(dir1(()))

print(dir1({}))

print(dir1(int))

print(dir1(''))

print(dir1([]))

print(dir1(set))

print(dir1(frozenset))

print(sys.__doc__)

print('*' * 10, 'SYS.PATH.__doc__', '*' * 10, '\n\n')

print(sys.path.__doc__)

print('\n\n', '*' * 10, 'string.__doc__', '*' * 10, '\n\n')

x = ''.__doc__

print(x)

