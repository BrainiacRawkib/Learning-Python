s = 'spammy'

s = s[:3] + 'xx' + s[5]

print(s)

s = 'spammy'

s = s.replace('mm', 'ss')

print(s)

s = s.__add__('nn')

print(s)


s = 'xxxxSPAMxxxxSPAMxxxx'

# where = s.find('SPAM')
#
# print(where)
#
# s = s[:where] + 'EGGS' + s[(where + 4):]

s = s.replace('SPAM', 'EGGS', 1)

print(s)


s = 'spammy'

l = list(s)

print(l)

l[3] = 'x'
l[4] = 'x'

print(l)

s = ''.join(l)

print(s)

x = 'SPAM'.join(['eggs', 'sausage', 'toast', 'french fries'])

print(x)

line = 'sdjkld'

print(line.isalpha())


