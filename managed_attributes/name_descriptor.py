class Name:
    """Name descriptor docs"""
    def __get__(self, instance, owner):
        print('fetching...', self.__class__.__name__, instance.__class__.__name__, instance._name, owner)
        return instance._name, instance._age

    def __set__(self, instance, value):
        print('changing...')
        instance._name = value
        print('setting instance value to : ', instance._name)

    def __delete__(self, instance):
        print('deleting attribute...')
        del instance._name


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __repr__(self):
        return '{}'.format(self.name)

    name = Name()  # instance state is per client instance


bob = Person('Bob Smith', 34)
# print(bob.name)
print(bob)
bob.name = 'Robert Smith'
# print(bob.name)
print(bob)
# del bob.name

