class A(type):
    def __getitem__(cls, item):
        return cls.data[item]

    def __getattr__(cls, i):
        return getattr(cls.data, i)


class B(metaclass=A):
    data = 'spam'
    date = 'spammer'


print(B[0], B.upper())

