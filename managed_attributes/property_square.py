class PropSquare:
    def __init__(self, start):
        self.val = start

    def getx(self):
        return self.val ** 2

    def setx(self, value):
        self.val = value

    x = property(getx, setx)


p = PropSquare(3)
q = PropSquare(32)


print(p.x)

p.x = 40

print(p.x)
print(q.x)
