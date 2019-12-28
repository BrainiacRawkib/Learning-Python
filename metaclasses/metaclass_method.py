class A(type):
    def a(cls):
        cls.x = cls.y + cls.z

    # def x(cls):
    #     print('ax', cls)
    #
    # def y(cls):
    #     print('ay', cls)


class B(metaclass=A):
    y, z = 11, 22

    @classmethod
    def b(cls):
        return cls.x

    # def y(self):
    #     print('by', self)
    #
    # def z(self):
    #     print('bz', self)


# B.x()
i = B()
# print(B.y, B.z)
# i.y(), i.z()
print(B.a(), B.x)

