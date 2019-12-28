from types import FunctionType
from metaclasses.decotools import tracer


def decorate_all(decorator):
    class MetaTrace(type):
        def __new__(meta, clsname, supercls, clsdict):
            for attr, attrval in clsdict.items():
                print(attr, ': ', attrval)
                if type(attrval) is FunctionType:
                    clsdict[attr] = decorator(attrval)
            return type.__new__(meta, clsname, supercls, clsdict)
    return MetaTrace


class Person(metaclass=decorate_all(tracer)):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    def last_name(self):
        return self.name.split()[-1]


bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)

print(bob.name, sue.name)

sue.give_raise(.10)

print('%.2f' % sue.pay)
print(bob.last_name(), sue.last_name())



