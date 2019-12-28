class Client1:
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


class Client2:
    value = 'ni?'


def eggs(obj):
    return obj.value * 4


def ham(obj, value):
    return value + 'ham'


Client1.eggs = eggs
Client1.ham = ham

Client2.eggs = eggs
Client2.ham = ham

x = Client1('Ni')
print(x.spam())
print(x.eggs())
print(x.ham('bacon'))

y = Client2()
print(y.eggs())
print(y.ham('bacon'))

