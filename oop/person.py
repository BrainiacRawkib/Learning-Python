"""
Record and process information about people.
Run this file directly to test its classes.
"""

from oop.classtools import AttrDisplay


class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def giveraise(self, percent):
        self.pay = int(self.pay * (1 + percent))
        return self.pay

    # def __repr__(self):
    #     return '[%s: %s, %s, %s]' % (self.__class__.__name__, self.name, self.pay, self.job)


class Manager(Person):
    """
    A customized Person with special requirements
    """

    def __init__(self, name):
        Person.__init__(self, name, 'mgr', 500000)

    def giveraise(self, percent, bonus=.10):
        return Person.giveraise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def give_raises(self, percent):
        for person in self.members:
            person.giveraise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


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

    print('\n---All Four--\n')
    for obj in (bob, sue, tom, otm):
        obj.giveraise(.10)
        print(obj)

    print('\n---Department---\n')

    development = Department(bob, sue)
    development.add_member(tom)
    development.give_raises(.10)
    development.show_all()


