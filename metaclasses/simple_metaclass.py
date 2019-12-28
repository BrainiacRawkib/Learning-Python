class MetaOne(type):
    def __new__(mcs, cls, supercls, clsdict):
        print('In MetaOne.new', mcs, cls, supercls, clsdict, sep='\n...')
        return type.__new__(mcs, cls, supercls, clsdict)


class Eggs:
    pass


print('Making class...')


class Spam(Eggs, metaclass=MetaOne):
    data = 1

    def meth(self, arg):
        return self.data + arg


print('Making instance...')
x = Spam()
print('data: ', x.data, x.meth(2))
# import time, sys

# for i in 'Making instance...':
#     print(i, end=' ')
#     sys.stdout.flush()
#     time.sleep(0.25)
