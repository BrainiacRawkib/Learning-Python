def eggs(obj):
    return obj.value * 4


def ham(obj, value):
    return value + 'ham'


class Extender(type):
    def __new__(meta, clsname, supercls, clsdict):
        clsdict['eggs'] = eggs
        clsdict['ham'] = ham
        return type.__new__(meta, clsname, supercls, clsdict)


class Client1(metaclass=Extender):
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


class Client2(metaclass=Extender):
    value = 'ni?'


x = Client1('Ni!')
print(x.spam())
print(x.eggs())
print(x.ham('bacon'))

y = Client2()
print(y.eggs())
print(y.ham('bacon'))


