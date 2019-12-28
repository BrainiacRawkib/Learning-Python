class Super:
    def method(self):
        print('I am Super Class...')


class Tool:
    def __method(self):
        return 'I am _Tool__method()'

    def other(self):
        print(self.__method())


class Sub1(Tool, Super):
    def actions(self):
        self.method()
        self.other()


class Sub2(Tool):
    def __init__(self):
        self.method = 99


i = Sub1()
i.actions()



