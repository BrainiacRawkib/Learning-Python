class Slicer:
    def __getitem__(self, item):
        print(item)

    def __getslice__(self, i, j):
        print(i, j)

    def __setslice__(self, i, j, sequence):
        print(i, j, sequence)


Slicer()[1]

Slicer()[1:9]

Slicer()[1:9:2]

