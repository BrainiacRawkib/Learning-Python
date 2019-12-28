class C:
    def __init__(self, x):
        self.x = x
        self.y = 2
        self.new()
        self.old()

    def new(self):
        self.a = 3
        self.b = 4

    def old(self):
        print('i am old...')
        # pass


x = C('x')

print(x.__dict__)


