instances = {}


def get_instances(obj):
    klass = obj.__class__
    print('Klass : ', klass)
    print('obj : ', obj.__dict__)
    if klass not in instances:
        instances[klass] = obj
        print(instances[klass])
    return instances[klass]


class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


bob = get_instances(Person('Bob', 40, 10))

print(bob)
