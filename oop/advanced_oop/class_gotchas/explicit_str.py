class ListTree:
    def __str__(self):
        return 'i am {} class. {}'.format(self.__class__.__name__, self.other())

    def other(self):
        return 'Inheriting from {}'.format(self.__class__.__bases__)


class Super:
    def __str__(self):
        return '{}'.format(self.__class__.__name__)

    def other(self):
        pass


class Sub(Super, ListTree):
    __str__ = ListTree.__str__
    other = ListTree.other

    # def other(self):
    #     return 'Inheriting from {}.other'.format(self.__class__.__bases__)


print(Sub())


