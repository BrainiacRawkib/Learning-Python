def typoerror(x, y):
    print(x + y)


try:
    # x = input('Enter for x: ')
    # y = input('Enter for y: ')
    typoerror([0, 1, 3], 'string')
except TypeError:
    print('A TypeError has been encountered!.')
print('Insert the same data type for x and y!')



