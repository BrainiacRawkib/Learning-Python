s = 'spam'

print(s[2:])

print(s[:1])

print(s[:2])

print(s[:3])

print(s[:4])

print('root' + s[:4])


for i in range(len(s)):
    x = s[i:]
    y = s[:i]
    z = s[i:] + s[:i]
    print(x, y, z, i, s[i], sep=' : ')


def scramble(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]


print(scramble('crabbing'))

print(scramble([1, 2, 3, 4, 5, 6]))


def gen_scramble(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]


print(list(gen_scramble('crabbing')))


