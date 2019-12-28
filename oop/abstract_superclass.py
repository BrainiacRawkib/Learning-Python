from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass


class Sub(Super):
    def action(self):
        print('spam...')


x = Sub()
x.delegate()

