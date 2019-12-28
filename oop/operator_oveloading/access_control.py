class AccessControl:

    def __setattr__(self, key, value):
        if key == 'age':
            self.__dict__[key] = value + 10
        else:
            raise AttributeError(key + ' not allowed')


x = AccessControl()

x.age = 40

print(x.age)

x.name = 'Bob'

