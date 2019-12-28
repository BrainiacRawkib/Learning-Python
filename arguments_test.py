def changer(a, b):
    a = 2  # a is changed by x
    b[0] = 'spam'  # b changes the first value in l (i.e in-place changes) b changes l in-place.


x = ['boo', 'foo']
l = ['crap', 'maps', 'spear']


changer(x, l)  # changer(x, l[:]) is used to pass a copy, so that l does not change

print(x, l)


L = [1, 2]

b = L

b[0] = 'spam'

print(L)


def f(x, *args, **kwargs):
    print(x, args, kwargs)


f(12)

f(30, 23, 'args', ['nice', 'one'], a=56, b='foo', c='bar', d=['dir', 'try'], e=('os', 'sys'))

s = {'a': 3, 'b': 900,}

x = s.get('b', 4)

print(x)


import bitwise_test