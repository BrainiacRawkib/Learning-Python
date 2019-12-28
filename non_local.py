def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested


f = tester(0)

f('spam')

f('ham')

f('crams')


# how to achieve the nonlocal effect in python 2.X but not really accurate as nonlocal


def tester2(start):
    global state

    state = start

    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested


f = tester(0)

f('maps')

f('pams')


# Class based alternative for python 2.x


class Tester:
    def __init__(self, start):
        self.state = start

    def nested(self, label):
        print(label, self.state)
        self.state += 1


f = Tester(0)

f.nested('cramps')

f.nested('cramper')

g = Tester(5)

g.nested('oops')

g.nested('fooo')


def test(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested


a = test(59)

a('fine')
a('good')
a('gooder')


def testing(start):
    def nested(label):
        print(label, state[0])
        state[0] += 1
    state = [start]
    return nested


from makeopen import makeopen


f = open('first_script.py')

f.read()
# makeopen('spam')




