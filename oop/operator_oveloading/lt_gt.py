class C:
    data = 'spam'

    def __gt__(self, other):
        return self.data > other

    def __lt__(self, other):
        return self.data < other


x = C()

print(x > 'ham')
print(x < 'ham')


class F:
    def __bool__(self):
        print('in bool...')
        return True


x = F()

print(bool(x))
