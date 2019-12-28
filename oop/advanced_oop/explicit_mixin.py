class A:
    def other(self):
        print('A.other.')


class Mixin(A):
    def other(self):
        print('Mixin.other.')
        # super(Mixin, self).other()
        A.other(self)


class B(A):
    def method(self):
        print('B.method.')


class C(Mixin, B):
    def method(self):
        print('C.method.')
        super(C, self).other()
        super(C, self).method()
        # Mixin.other(self)
        # B.method(self)


Mixin().other()
C().method()

print(C.__mro__)
