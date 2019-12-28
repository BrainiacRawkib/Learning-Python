s = 'spamming'

for i in range(len(s)):
    x = s[i:] + s[:i]
    print(x, end=' ')

print()

for x in s[::2]:
    print(x, end=', ')

print()

l = [1, 2, 3, 4, 5]

for x in range(len(l)):
    l[x] += 1

print(l)

l = [x + 1 for x in l]

print(l)


