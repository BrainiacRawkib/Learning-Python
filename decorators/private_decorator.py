trace_me = False


def trace(*args):
    if trace_me:
        print('[' + ' '.join(map(str, args)) + ']')


def private(*privates):
    def on_decorator(klass):
        class OnInstance:
            def __init__(self, *args, **kwargs):
                self.wrapped = klass(*args, **kwargs)

            def __getattr__(self, item):
                trace('get:', item)
                if item in privates:
                    raise TypeError('Private attribute fetch: ' + item)
                else:
                    return getattr(self.wrapped, item)

            def __setattr__(self, key, value):
                trace('set: ', key, value)
                if key == 'wrapped':
                    self.__dict__[key] = value
                elif key in privates:
                    raise TypeError('Private attribute change: ' + key)
                else:
                    print(self.wrapped, key, value)
                    setattr(self.wrapped, key, value)
        return OnInstance
    return on_decorator


if __name__ == '__main__':
    trace_me = True

    @private('data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start

        def size(self):
            return len(self.data)

        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2

        def display(self):
            print('%s => %s' % (self.label, self.data))


    x = Doubler('X is ', [1, 2, 3])
    y = Doubler('Y is ', [-10, -20, -30])

    print(x.label)
    x.display()
    x.double()
    x.display()

    print(y.label)
    y.display()
    y.double()
    y.label = 'Spam'
    # y.data = 90  # remove data from the decorator for this line to work
    y.display()

