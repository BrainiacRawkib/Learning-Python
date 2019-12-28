class Indexer:
    def __getitem__(self, index):
        return index ** 2


x = Indexer()

print(x[2])

for i in range(5):
    print(x[i], end=' ')


print('\n\n', '**' * 10)


class Slicer:
    data = [5, 6, 7, 8, 9]

    # def __init__(self, *value):
    #     self.data = list(value)

    # def advance oop(self, *v):
    #     self.data = list(v)

    def __getitem__(self, index):
        print('getitem: ', index)
        return self.data[index]


# x = Slicer(23, 45, 67, 89, 34, 1, 3)

x = Slicer()

# x.advance oop(23, 45, 67, 89, 34, 1, 3)

# x.advance oop('crippy', 'crap')

print(x[0])

print(x[1])

print(x[-1])

print(x[2:4])

print(x[:-1])

print(x[::-1])

print(x[:3])


print('\n\n', '**' * 10, 'Indexer2',  '**' * 10, '\n')


class Indexer2:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('Indexing', index)
        else:
            print('Slicing ', index.start, index.stop, index.step)


x = Indexer2()

x[1:]


x[1:99:2]


print('\n\n', '**' * 10, 'IndexSetter',  '**' * 10, '\n')


class IndexSetter:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print('getitem: ', index)
        return self.data[index]

    def __setitem__(self, key, value):
        self.data[key] = value


x = IndexSetter()

x[0] = 34

print(x[0])

x[1] = 94

print(x[1])

x[-1] = 300

print(x[-1])

