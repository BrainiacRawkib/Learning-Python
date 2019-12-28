trace_me = False


def trace(*args):
    if trace_me:
        print('[' + ' '.join(map(str, args)) + ']')


class BuiltinsMixin:
    def __str__(self):
        return str(self.__wrapped)

    def __add__(self, other):
        return self.__wrapped + other

    def __getitem__(self, item):
        return self.__wrapped[item]

    def __call__(self, *args, **kwargs):
        return self.__wrapped(*args, **kwargs)


class BuiltinsMixin2:
    def __str__(self):
        return self.__class__.__getattr__(self, '__str__')()

    def __add__(self, other):
        return self.__class__.__getattr__(self, '__add__')(other)

    def __getitem__(self, item):
        return self.__class__.__getattr__(self, '__getitem')[item]

    def __call__(self, *args, **kwargs):
        return self.__class__.__getattr__(self, '__call__')(*args, **kwargs)


def access_control(failif):
    def on_decorator(klass):
        class OnInstance(BuiltinsMixin):
            def __init__(self, *args, **kwargs):
                self.__wrapped = klass(*args, **kwargs)

            def __getattr__(self, item):
                trace('get: ', item)
                if failif(item):
                    raise TypeError('Private attribute fetch: ' + item)
                else:
                    return getattr(self.__wrapped, item)

            def __setattr__(self, key, value):
                trace('set: ', key, value)
                if key == '_OnInstance__wrapped':
                    self.__dict__[key] = value
                elif failif(key):
                    raise TypeError('Private attribute change: ' + key)
                else:
                    setattr(self.__wrapped, key, value)
        return OnInstance
    return on_decorator


def private(*attributes):
    return access_control(failif=(lambda attr: attr in attributes))


def public(*attributes):
    return access_control(failif=(lambda attr: attr not in attributes))


if __name__ == '__main__':
    @private('age')
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age


    x = Person('Bob', 40)
    print(x.name)


