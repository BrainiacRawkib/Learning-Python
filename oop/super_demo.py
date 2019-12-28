class Super:
    def method(self):
        print('in the Super.method')

    def delegate(self):
        self.action()


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('in the Replacer.method')


class Extender(Super):
    def method(self):
        print('starting Extending.method')
        Super.method(self)
        print('ending the Extender.method')


class Provider(Super):
    def action(self):
        print('in the Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()


# class Superb:
#     def delegate(self):
#         self.action()
#
#     def action(self):
#         raise NotImplementedError('action not exist!')
#
#
# class Sub(Superb):
#     def action(self):
#         print('spam')
#
#
# x = Sub()
#
#
# x.delegate()


