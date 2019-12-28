import time


def tracer(func):
    calls = 0

    def on_call(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('Call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return on_call


def timer(label='', trace=True):

    def on_decorator(func):

        def on_call(*args, **kwargs):
            start = time.clock()
            result = func(*args, **kwargs)
            elapsed = time.clock() - start
            on_call.alltime += elapsed

            if trace:
                format = '%s%s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, on_call.alltime)
                print(format % values)
            return result
        on_call.alltime = 0
        return on_call
    return on_decorator


if __name__ == '__main__':
    class Person:
        @tracer
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay

        @tracer
        def give_raise(self, percent):
            self.pay *= (1.0 + percent)

        @tracer
        def last_name(self):
            return self.name.split()[-1]

    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)

    print(bob.name, sue.name)
    sue.give_raise(.10)

    print('%.2f' % sue.pay)
    print(bob.last_name(), sue.last_name())


