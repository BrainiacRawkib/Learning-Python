s = 'spamatozoa'

print(s.find('pam'))

print(s.find('map'))

replace = s.replace('pam', 'perm')

print(replace)


line = 'aaa,bbb,ccc,ddd\n'

print(line.rstrip().split(','))

line = 'aaa,bbb,ccc,ddd\n,eee'

print(line.rsplit())
