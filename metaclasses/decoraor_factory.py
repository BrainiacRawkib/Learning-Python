from types import FunctionType
from metaclasses.decotools import tracer, timer


def decorate_all(decorator):
    def deco_decorate(klass):
        for attr, attrval in klass.items():
            if type(attrval) is FunctionType:
                setattr(klass, attr, decorator(attrval))
        return klass
    return deco_decorate


@decorate_all(tracer)
class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    def last_name(self):
        return self.name.split()[-1]



