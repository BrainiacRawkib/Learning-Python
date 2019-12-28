profile = open('profile.txt', 'a')

x = 'Single'

y = 23

z = 'Dev, Hacker'

print(x, y, z, sep=', ', file=profile)

print(open('profile.txt').read())



