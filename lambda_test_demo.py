x = lambda a='spam', b='ham', c='jam': a + b + c


print(x('brick'))


def knights():
    title = 'Sir'
    action = lambda x: title + ' ' + x
    return action


act = knights()

print(act('Cricket'))

L = [
     lambda x: x **2,
     lambda x: x **3,
     lambda x: x **4
     ]


for f in L:
    print(f(2))


print(L[0](3))


print('\n\n', '*' * 30, '\n\n')


key = 'got'

x = {
    'already': (lambda: 2 + 2),
    'got': (lambda: 2 * 4),
    'one': (lambda: 2 ** 6)
    }[key]()

print(x)

print('***' * 10)

import sys

showall = lambda x: list(map(sys.stdout.write, x))

t = showall(['spam\n', 'toast\n', 'eggs\n'])


show_all = lambda a: [sys.stdout.write(line) for line in a]

t = show_all(('bright\n', 'side\n', 'of\n', 'life\n'))


print('\n\n', '*' * 30, '\n\n')


show = lambda x: print(*x, sep='', end='')


a = show(('good\n', 'part\n', 'of\n', 'wealth\n'))


def action(x):
    return lambda y: x + y


act = action(99)
print(act(101))


action = lambda x: lambda y: x + y

act = action(80)

print(act(98))

