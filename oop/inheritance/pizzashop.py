from oop.inheritance.employees import PizzaRobot, Server


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, 'orders from', server)

    def pay(self, server):
        print(self.name, 'pays for item to', server)


class Oven:
    def bake(self):
        print('oven bakes')


class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')  # Embed other objects
        self.chef = PizzaRobot("Bob")  # A robot named Bob
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)  # Activate other objects
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

    def re(self):
        print('\n', '**' * 10, 'Calling self.order', '**' * 10, '\n')
        return self.order('returned')


if __name__ == '__main__':
    scene = PizzaShop()  # Make the composite
    scene.order('Homer')
    scene.re()
    print('.......')
    scene.order('Shaggy')
    scene.re()



