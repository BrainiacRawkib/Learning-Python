class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, item):
        print('Trace: ' + item)
        return getattr(self.wrapped, item)


x = Wrapper([1, 2, 3, 4, 5])

a = [45, 6, 7, 90]
x.extend(a)

print(x.wrapped)
