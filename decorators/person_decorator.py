class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('Call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args, **kwargs)


def tracer(func):
    calls = 0

    def on_call(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('Call %s to %s' % (calls, func.__name__))
        print('*args: ', *args, '**kwargs: ', **kwargs)
        return func(*args, **kwargs)
    return on_call


class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def last_name(self):
        return self.name.split()[-1]

    @tracer
    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))
        return self.pay


bob = Person('Bob Smith', 500000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.give_raise(.10)  # Runs onCall(sue, .10)
print(int(sue.pay))
print(bob.last_name(), sue.last_name())
# print(bob.give_raise(.10), int(bob.pay))

