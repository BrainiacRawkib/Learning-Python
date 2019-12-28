class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        print(self, self.__class__.__name__)
        return self.hours * self.rate


x = Person('we', 90, 34)
print(x.__dict__)
print(x.pay())

