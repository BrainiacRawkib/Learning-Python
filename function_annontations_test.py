def func(a: 'spam', b, c: 99) -> int:
    return a + b + c


print(func(1, 2, 3))

print(func.__annotations__)

for arg in func.__annotations__:
    print(arg, '-->', func.__annotations__[arg])


print('\n\n', '*' * 30, '\n\n')


def func2(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c


print(func2(1, 2, 3))
print(func2())
print(func2.__annotations__)

