class Test:
    def __init__(self):
        self.x = 1
        self.y = 3

    def meth(self):
        pass

    def attr(self):
        for attr in dir(self):
            if not (attr.startswith('__') and attr.endswith('__')):
                print(attr)


i = Test()

i.attr()
