class C:
    x = 33

    def m(self):
        x = 44
        self.x = 55
        return x, self.x

    def n(self):
        return self.x, C.x


if __name__ == '__main__':
    i = C()
    print(i.m())
    print(i.n())


def h2():
    x = 33

    def nested():
        nonlocal x
        x = 99
        return x
    return nested()


x = h2()
print(x)
