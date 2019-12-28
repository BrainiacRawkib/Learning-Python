class StepperIndex:
    def __getitem__(self, item):
        return self.data[item]


x = StepperIndex()

x.data = 'spam'

print(x[1])

for i in x:
    print(i, end=' ')

print()

print(list(map(str.upper, x)))


list(x)

print(''.join(x))

