class MetaTwo(type):
    def __new__(mcs, cls, supercls, clsdict):
        print('In MetaTwo: ', mcs, cls, supercls, clsdict, sep='\n...')
        return type.__new__(mcs, cls, supercls, clsdict)

    def __init__(cls, clsname, supercls, clsdict):
        print('In MetaTwo.init: ', clsname, supercls, clsdict, sep='\n...')
        print('...init class object:', list(cls.__dict__.keys()))


class Eggs:
    pass


print('Making Class...')


class Spam(Eggs, metaclass=MetaTwo):
    data = 1

    def meth(self, arg):
        return self.data + arg


print('Making instance...')

x = Spam()
print('data: ', x.data, x.meth(2))

