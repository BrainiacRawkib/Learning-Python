class DescInstState:
    def __init__(self, data):
        self.data = data

    def __get__(self, instance, owner):
        print('Descriptor Value: ', self.__class__.__name__, self.data)
        print('Client Class Value: ', instance.__class__.__name__, instance._data)
        return '%s %s' % (self.data, instance._data)

    def __set__(self, instance, value):
        instance._data = value


class Client:
    def __init__(self, data):
        self._data = data

    managed = DescInstState('spam')


i = Client('eggs')

print(i.managed)

i.managed = 'spammer'
print(i.managed)

