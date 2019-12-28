l = [1]

l[:0] = [2, 3, 4]

print(l)

l = ['abc', 'ABD', 'aBe']

l.sort()

print(l)

# l = ['abc', 'ABD', 'aBe']

l.sort(key=str.lower)

print(l)


x = sorted(l, key=str.lower, reverse=True)

print(x)

l.append(['wer', 'rew'])

print(l)

l = ['abc', 'ABD', 'aBe']

l.extend(['wer', 'rew'])

print(l)

l.insert(1, 'meg')

print(l)

l = ['abc', 'ABD', 'aBe']

x = sorted([x.lower() for x in l], reverse=True)

print(x)

x = ['advance oop', 'guy', 'here', 'got', 'one']

print(x)

x[1:] = []

print(x)

x[0] = []

print(x)

