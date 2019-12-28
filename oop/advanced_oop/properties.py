class Properties:
    def getage(self):
        return 40

    def setage(self, value):
        print('set age: %s' % value)
        self._age = value

    age = property(getage, setage, None, None)


x = Properties()

print(x.age)

x.age = 42

print(x.age)

print(x._age)

x.job = 'trainer'

print(x.job)

