from oop.advanced_oop.class_method import Spam


class Sub(Spam):
    num_instances = 0

    def print_num_instances(cls):
        print('Extra Stuff...', cls)
        Spam.print_num_instances()

    print_num_instances = classmethod(print_num_instances)


class Other(Spam):
    pass


x = Sub()
y = Spam()
x.print_num_instances()

y.print_num_instances()

z = Other()

z.print_num_instances()

