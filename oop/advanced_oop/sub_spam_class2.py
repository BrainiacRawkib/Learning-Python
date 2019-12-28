class Spam:
    num_instances = 0

    def count(cls):
        cls.num_instances += 1

    def __init__(self):
        self.count()

    count = classmethod(count)


class Sub(Spam):
    # num_instances = 0
    pass
    # def __init__(self):
    #     Spam.__init__(self)


class Other(Spam):
    # num_instances = 0
    pass


x = Spam()

y1, y2 = Sub(), Sub()  # these 2 instances plus x = Spam() instance give us 3 since it inherits from Spam

z1, z2, z3 = Other(), Other(), Other()  # these 3 instances plus x = Spam() instance gives us 4

print(x.num_instances, y1.num_instances, z1.num_instances)



