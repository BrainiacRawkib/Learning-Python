class Base(Exception):
    def __str__(self):
        return '{} is the exception...'.format(self.__class__.__name__)


try:
    raise Base()
except Base as x:
    print(x)


# raise Base()
Base()
