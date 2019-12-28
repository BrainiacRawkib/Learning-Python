class Super:
    def method(self):
        print('\nIn The Super Method...\n')


class Sub(Super):
    def method(self):
        print('starting from the Sub method...')
        Super.method(self)
        print('ending Sub method...')


if __name__ == '__main__':
    x = Sub()
    x.method()


print('\n', '**' * 30, '\n')


class Superb:
    def hello(self):
        self.data1 = 'spam'


class Subb(Superb):
    def hola(self):
        self.data2 = 'eggs'
        # self.hip = h


i = Subb()

# print(i.__dict__)  # it will only print data2 as key on first execution if the __init__ constructor is initialized in
# # the class
#
#
# i = Subb()
#
# print(list(i.__dict__))
#
# i = Subb()
#
# print(i.__dict__)

i.hello()

print(i.__dict__)

i.hola()

print(i.__dict__)


print(list(x for x in Subb.__dict__.keys() if not x.startswith('__')))

print(list(Superb.__dict__.keys()))

print(i.data1)

i.__dict__['data3'] = 'hams'

print(i.data3)


