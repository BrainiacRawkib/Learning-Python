d = {'a': 12, 'c': 34, 'b': 45, 'e': 54}

print(sorted(d))

for key in sorted(d):
    print(key, '---> ', d[key])
