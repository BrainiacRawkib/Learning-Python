lines = [line.rstrip() for line in open('datafile.txt', 'r')]

print(lines)

lines = [line.rstrip().split() for line in open('datafile.txt', 'r')]

print(lines)

lines = [line.rstrip().upper() for line in open('datafile.txt', 'r')]

print(lines)

lines = [line.rstrip().replace(' ', '!') for line in open('datafile.txt', 'r')]

print(lines)

lines = [('sys' in line, line[:5]) for line in open('url_open.py', 'r')]

print(lines)


lines = [line.rstrip() for line in open('datafile.txt', 'r') if line[0] == 'S']

print(lines)

lines = [line.rstrip() for line in open('datafile.txt', 'r') if line.rstrip()[-1].isalnum()]

print(lines)

f = len(open('datafile.txt').readlines())

print(f)

f = len(open('datafile_2.txt').readline())

print(f)

f = len(open('datafile_2.txt').read())

print(f)

x = len([line for line in open('datafile.txt') if line.strip() != ''])

print(x)

import functools, operator

x = functools.reduce(operator.add, open('datafile.txt'))

print(x)

x = list(open('datafile.txt'))

print(x)

x = tuple(open('datafile.txt'))

print(x)

x = '&&'.join(open('datafile.txt'))

print(x)

a, b, c = open('datafile.txt')

print(a, b, c)

a, *b = open('datafile.txt')

print(a, b)

x = 'SPAM\n' in open('datafile.txt')

print(x)

x = 'SPAM' in open('datafile.txt')

print(x)

x = [11, 22, 33, 44]

x[1:3] = open('datafile.txt')

print(x)

a = [11]

a.extend(open('datafile.txt'))

print(a)

i = min(open('datafile.txt'))

print(i)

x = max(open('datafile.txt'))

print(x)


