x = 1  # 1 decimal is 0001 in bits


# x = x << 2  # Shift left 2 bits: 0100
#
# print(x)

# x |= 2  # Bitwise OR (either bit=1): 0011
#
# print(x)

# x &= 1  # Bitwise AND (both bits=1): 0001

#
print(x)


num_bin = bin(x)

bit_len = x.bit_length()

print(num_bin)


print(bit_len)

bit_leng = len(bin(x)) - 2

print(bit_leng)


r = round(2.4567787, 3)

print(r)

