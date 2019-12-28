B = bytearray(b'spam')

B.extend(b'eggs')

print(B)

# B.decode()

print(B.decode())  # decoding bytearray removes 'bytearray from printing at the output and translate it to normal string


