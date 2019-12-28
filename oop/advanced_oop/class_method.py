class Spam:
    num_instances = 0

    def __init__(self):
        Spam.num_instances += 1

    def print_num_instances(cls):
        print('Number of instances: %s' % cls.num_instances, cls)

    print_num_instances = classmethod(print_num_instances)


a = Spam()
b = Spam()

# a.print_num_instances()

