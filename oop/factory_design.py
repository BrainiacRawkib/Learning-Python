def factory(klass, *args, **kwargs):
    return klass(*args, **kwargs)


class Spam:
    def doit(self, message):
        print(message)


class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job

    def __repr__(self):
        return 'name: {}, job: {}'.format(self.name, self.job)


obj1 = factory(Spam)
obj2 = factory(Person, 'Arthur', 'King')
obj3 = factory(Person, 'Brian')

obj1.doit(98)
print(obj2)
print(obj3)


