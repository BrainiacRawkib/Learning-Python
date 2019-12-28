r = range(6)

i = iter(r)

print(next(i))

print(next(i))

x = iter(r)  # Two iterators on one range, by contrast zip, map, filter do not support multiple iterators on the same
# result

print(next(x))

print(next(x))

print(next(x))

print(next(x))


