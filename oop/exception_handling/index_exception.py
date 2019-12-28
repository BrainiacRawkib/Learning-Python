def fetcher(obj, index):
    return obj[index]


x = 'spammer'

# print(fetcher(x, 50))

try:
    # print(fetcher(x, 5))
    # print(fetcher(x, 50))
    raise IndexError
except IndexError:
    print('Index out of bound!!!')


x = 3, 9, 4

print(x)
