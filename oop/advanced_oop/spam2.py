class Spam:
    num_instances = 0

    def __init__(self):
        Spam.num_instances += 1

    # @staticmethod
    def print_num_instances():
        print("Number of instances: %s" % Spam.num_instances)

    print_num_instances = staticmethod(print_num_instances)


a = Spam()
b = Spam()
c = Spam()

Spam.print_num_instances()

a.print_num_instances()

