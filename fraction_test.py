# from fractions import Fraction
#
#
# f = Fraction(2, 3)
#
# print(f)
#
# print(f + 1)
#
# print(f + Fraction(1, 2))
#
#

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def giveraise(self, percent):
        self.pay *= (1.0 + percent)


bob = Worker('Bob smith', 50000)
bo = bob.lastname()

print(bo)
print((1.0 + .10) * 60000)
print(6000 * 11)


