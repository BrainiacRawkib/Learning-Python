class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def klass(self):
        return 'Class {}'.format(self.__class__.__name__)

    def __repr__(self):
        return 'Person: %s  %s' % (self.name, self.pay)


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)  # Embed a Person object

    def give_raise(self, percent, bonus=.10):
        self.person.give_raise(percent + bonus)  # Intercept and delegate

    def klass(self):
        return 'Class {}'.format(self.__class__.__name__)

    def __getattr__(self, item):
        return getattr(self.person, item)  # Delegate all other attrs

    def __repr__(self):
        return str(self.person)  # Must overload again (in 3.x)


if __name__ == '__main__':
    sue = Person('Sue Jones', job='dev', pay=100000)
    sue.give_raise(.10)
    print(sue)

    tom = Manager('Tom Jones', 500000)
    print(tom.klass())
    print(tom.last_name())
    tom.give_raise(.10)
    print(tom)


