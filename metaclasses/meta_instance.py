class MetaOne(type):
    def __new__(meta, clsname, supercls, clsdict):
        print('In MetaOne.new:', clsname)
        return type.__new__(meta, clsname, supercls, clsdict)

    def toast(self):
        return 'toast'


class Super(metaclass=MetaOne):
    def spam(self):
        return 'spam'


class Sub(Super):
    def eggs(self):
        return 'eggs'


i = Super
x = Sub()
print(x.spam(), x.eggs())
print(i.mro(), i.toast(), Sub.toast(), Sub.mro())
