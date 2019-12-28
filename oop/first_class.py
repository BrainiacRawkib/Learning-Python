class FirstClass:
    value = 0

    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


i = FirstClass()

print(i.value)


i = FirstClass()

i.setdata('default')

i.display()

i.data = 'New Value'

i.display()


class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)


z = SecondClass()

z.setdata('crappy')

z.display()

print('\n')


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data.__add__(other))

    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    def __mul__(self, other):  # In-place change: named
        self.data *= other


a = ThirdClass('abc')  # __init__ called
a.display()  # Inherited method called

print(a)  # __str__: returns display string

print('\n')

b = a + 'xyz'  # __add__: makes a advance oop instance
b.display()  # b has all ThirdClass methods

print(b)  # __str__: returns display string

print('\n')

a.__mul__(3)  # mul: changes instance in place
print(a)

print('\n')

print(list(FirstClass.__dict__.keys()))

print('\n')

print(list(SecondClass.__dict__.keys()))

print('\n')

print(list(ThirdClass.__dict__))

print('\n')

print(list(x for x in FirstClass.__dict__.keys() if not x.startswith('__')))

print('\n')

print(list(x for x in SecondClass.__dict__.keys() if not x.startswith('__')))

print('\n')

print(list(x for x in ThirdClass.__dict__.keys() if not x.startswith('__')))

print('\n', '*' * 10, '\nInstance to class link ', '\n', '*' * 10)

print(i.__class__)

print(z.__class__)

print(a.__class__)


print('\n', '*' * 10, '\nClass to Superclasses link ', '\n', '*' * 10)

print(FirstClass.__bases__)

print(SecondClass.__bases__)

print(ThirdClass.__bases__)


def uppername(obj):
    return obj.upper()


s = uppername('crippy')

print(s)

x = 90

y = 100

res = x if x < y else y

print(res)

