class C:
    shared = []

    def __init__(self):
        self.perobj = []


x = C()
y = C()

print(x.shared, y.shared)

x.shared.append('spam')
x.perobj.append('spammer')

print(x.shared, x.perobj)

print(y.shared, y.perobj)

print(C.shared)
