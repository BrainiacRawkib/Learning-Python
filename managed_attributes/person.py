class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        try:
            print('fetching...')
            return self._name
        except AttributeError:
            print('No attribute found!')

    def set_name(self, value):
        print('changing...')
        self._name = value

    def del_name(self):
        print('deleting...')
        del self._name

    name = property(get_name, set_name, del_name, 'name property docs')


class LitPerson(Person):
    pass


bob = Person('Bob Smith')

print(bob.name)

bob.name = 'Robert Smith'

print(bob.name)

del bob.name

print(bob.name)

print('-'*20)

sue = Person('Sue Jones')

print(sue.name)

print(Person.name.__doc__)

print('-'*20)

jones = LitPerson('Jonah Jones')

print(jones.name)

