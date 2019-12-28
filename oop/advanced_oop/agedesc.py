class AgeDesc:
    def __get__(self, instance, owner):
        return 40

    def __set__(self, instance, value):
        instance._age = value


class Descriptors:
    age = AgeDesc()


x = Descriptors()

print(x.age)

x.age = 43

print(x._age)


