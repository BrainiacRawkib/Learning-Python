import time


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
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay

        @timer()
        def give_raise(self, percent):
            self.pay *= (1.0 + percent)

        @timer(label='***')
        def last_name(self):
            return self.name.split()[-1]

    bob = Person('Bob Smith', 50000)
    bob.give_raise(.10)

    print(int(bob.pay))
    print(bob.last_name())
