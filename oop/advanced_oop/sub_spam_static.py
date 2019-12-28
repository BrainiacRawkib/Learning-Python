from oop.advanced_oop.spam2 import Spam


class Sub(Spam):
    def print_num_instances():
        print('Extra stuff...')
        Spam.print_num_instances()

    print_num_instances = staticmethod(print_num_instances)


a = Sub()
b = Sub()

# a.print_num_instances()





