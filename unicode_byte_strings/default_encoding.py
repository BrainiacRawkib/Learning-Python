import sys


x = sys.getdefaultencoding()

print(x)

print(chr(196))

print(type(chr(196)))

b = b'spam'

print(b[0])  # indexing returns an int for bytes

print(b[0:])  # slicing returns a bytes or str object

print(list(b))

