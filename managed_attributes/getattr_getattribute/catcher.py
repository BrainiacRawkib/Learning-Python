class Catcher:
    def __getattr__(self, item):
        print('Getting: %s' % item)

    def __setattr__(self, key, value):
        print('Setting: %s = %s' % (key, value))


x = Catcher()

print(x.job)

print('---'*20)
print(x.pay)

print('---'*20)

x.pay = 99
print(x.pay)

