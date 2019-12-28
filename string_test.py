s = 'iamaprof'


print(s[1::2])

print(s[slice(1, None)])

print('\f\a\r')


menu = '''
this is the  # commenting nice
advance oop menu  # commenting
'''

print(menu)


x = 'spam' in 'abcdspm'

print(x)

c = ord('9')

print(c)

x = ord('5') - ord('0')

print(x, '\n\n')

b = '1101'
i = 0
while b != '':
    print('b : ', b)
    print('b[0] : ', b[0])
    i = i * 2 + (ord(b[0]) - ord('0'))
    b = b[1:]
    print('b[1:] : ', b)
    print('i : ', i, '\n')


print(i)

s = 'spam'

s = s + 'SPAM!'

print(s)

s = s[4:-1] + 'Burger' + s[-1]

print(s)


print(int('1101', 2))
print(int('1101', 3))
print(int('1101', 8))
print(int('1101', 16))

