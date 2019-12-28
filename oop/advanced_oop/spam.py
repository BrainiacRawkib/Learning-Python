class Spam:
    num_instances = 0

    def __init__(self):
        Spam.num_instances = Spam.num_instances + 1

    def print_num_instances(self):
        print('Number of instances created: %s' % Spam.num_instances)


a = Spam()
b = Spam()
c = Spam()

Spam.print_num_instances(a)

