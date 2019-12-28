x = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]

print(x)

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

N = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]

res = []

for row in M:
    tmp = []
    for col in row:
        tmp.append(col + 10)
    res.append(tmp)


print(res)


x = [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]


print(x)


def saver(x=[]):
    x.append(1)
    print(x)


saver([2])
saver()
saver()
saver()


print('**' * 10, 'saver2', '**' * 10)


def saver2(x=None):
    if x is None:
        x = []
    x.append(1)
    print(x)


saver2([2])
saver2()
saver2()


def saver_retention():
    saver_retention.x.append(1)
    print(saver_retention.x)


saver_retention.x = []

saver_retention()
saver_retention()
