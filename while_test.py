x = 'spam mail'

while x:
    print('x[0] : ', x[0])
    print('x : ', x)
    x = x[1:]
    print('x[1:] : ', x, '\n')


x = 10

# while x:
#     x -= 1
#     if x % 2 == 0:
#         print(x, end=' ')

while x:
    x -= 1
    if x % 2 != 0:
        continue
    print(x, end=' \n')


# Prime numbers
a = []
y = 100
x = y // 2  # // is used for floor division in order not to get floating number

while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        # break

        a.append(x)
    x -= 1
else:
    print(y, 'is prime')

print(a)


def match(x, value):
    for s in x:
        if s == value:
            return s


x = ['oer', '', 'op', 'v']

i = 'over'

while x:
    if match(x[0], i):
        print(i, 'Found!!!')
        break
    x = x[1:]
else:
    print(i, 'Not found!!!')

file = open('datafile.txt', 'r')

while file:  # while True
    char = file.read(1)
    if not char:
        break
    print(char)

file = open('datafile.txt', 'r')

while True:
    line = file.readline()
    if not line:
        break
    print(line.rstrip())




