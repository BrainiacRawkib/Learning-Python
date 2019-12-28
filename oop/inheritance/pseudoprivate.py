class C1:
    def meth1(self):
        self.__x = 88

    def meth2(self):
        print(self.__x)


class C2:
    def metha(self):
        self.__x = 99

    def methb(self):
        print(self.__x)


class C3:
    def methx(self):
        self._x = 99

    def methy(self):
        print(self._x)


class C4(C1, C2, C3):
    pass


i = C4()

i.meth1()
i.metha()
i.methx()

print(i.__dict__)

i.meth2()
i.methb()
i.methy()

print(i.__dict__)
