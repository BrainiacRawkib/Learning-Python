class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def giveraise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s, %s]' % (self.name, self.pay, self.job)


class Manager(Person):
    def __init__(self, name):
        # Person.__init__(self, name, 'mgr', 500000)
        self.person = Person(name, 'mgr', 500000)

    def giveraise(self, percent, bonus=.10):
        Person.giveraise(self, percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __repr__(self):
        return str(self.person)


if __name__ == '__main__':
    # self-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', ['dev', 'cto'], pay=100000)

    print(bob)
    print(sue)
    print(bob.lastname(), sue.lastname())

    sue.giveraise(.10)
    print(sue)

    tom = Manager('Tom Jones')
    tom.giveraise(.10)

    print(tom.lastname())
    print(tom)

    otm = Manager('Otm Mot')

    print(otm)

    print('\n---All three--\n')
    for obj in (bob, sue, tom, otm):
        obj.giveraise(.10)
        print(obj)


