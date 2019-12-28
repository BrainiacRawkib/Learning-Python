class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return '{}, {} receives {} as salary'.format(self.name, self.__class__.__name__, self.salary)


class Chef1(Employee):
    def __init__(self, name):
        super().__init__(name, 50000)


class Server1(Employee):
    def __init__(self, name):
        super(Server1, self).__init__(name, salary=40000)


class Chef2(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)


class Server2(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, salary=40000)


class TwoJobs(Server1, Chef1):
    def __init__(self, name):
        Employee.__init__(self, name, 70000)


bob = Chef1('Bob')
sue = Server1('Sue')
foo = TwoJobs('Foo')

print(bob)
print(sue)
print(foo)

