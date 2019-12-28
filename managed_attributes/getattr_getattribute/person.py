class Person:
    def __init__(self, name):
        self._name = name

    # def __getattr__(self, attr):
    #     print('__getattr__: ' + attr)
    #     if attr == 'name':
    #         return self._name
    #     else:
    #         raise AttributeError(attr)

    def __getattribute__(self, item):
        print('__getattribute__: ' + item)
        if item == 'name':
            item = '_name'
        return object.__getattribute__(self, item)  # avoid looping

    def __setattr__(self, key, value):
        print('__setattr__: ' + key)
        if key == 'name':
            key = '_name'  # inserting an else: condition would make key unusable by self.__dict__[key]
        self.__dict__[key] = value  # this defaults to self._name = value, then sends it to getattr, getattribute

    def __delattr__(self, item):
        print('deleting...: ' + item)
        if item == 'name':
            item = '_name'
        del self.__dict__[item]


bob = Person('Bob Smith')
print(bob.name)

bob.name = 'Robert Smith'
print(bob.name)

bob.age = 45
print(bob.age)

del bob.name
