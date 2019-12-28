class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('Call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        return Wrapper(self, instance)


class Wrapper:
    def __init__(self, desc, subj):
        self.desc = desc
        self.subj = subj

    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @Tracer
    def last_name(self):
        return self.name.split()[-1]

    @Tracer
    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))
        return self.pay


bob = Person('Bob Smith', 500000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.give_raise(.10)  # Runs onCall(sue, .10)
print(int(sue.pay))
print(bob.last_name(), sue.last_name())

