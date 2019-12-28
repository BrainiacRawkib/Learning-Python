items = ['aaa', 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
    if key in items:
        print(key, 'was found!')
    else:
        print(key, 'not found!')


seq1 = 'scam'
seq2 = 'spam'

res = []

for x in seq1:
    if x in seq2:
        res.append(x)


print(res)

res = [x for x in seq1 if x in seq2]

print(res)

for char in open('datafile.txt'):
    print(char)


