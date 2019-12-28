x = list(filter((lambda x: x > 0), [0, 0, 23, 3, 4, 56, -1, -19]))

print(x)

res = []
for x in range(-5, 5):
    if x > 0:
        res.append(x)

print(res)

x = [x for x in range(-10, 9) if x < 0]

print(x)
