s = 'eggs'

print(s.encode())

x = bytes(s, encoding='ascii')

print(x)

b = b'spam'

print(b.decode())

x = str(b, encoding='ascii')

print(x)

x = str(b, encoding='utf16')

print(x)

s = '\xc4\xe8'
print(s)

