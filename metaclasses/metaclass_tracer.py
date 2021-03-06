def tracer(clsname, supercls, clsdict):
    klass = type(clsname, supercls, clsdict)

    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = klass(*args, **kwargs)

        def __getattr__(self, item):
            print('Trace: ', item)
            return getattr(self.wrapped, item)
    return Wrapper


class Person(metaclass=tracer):
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


bob = Person('Bob', 40, 50)
print(bob.name)
print(bob.pay())

