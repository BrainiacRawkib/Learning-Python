import traceback


def inverse(x):
    return 1 / x


try:
    inverse(0)
except ZeroDivisionError:
    traceback.print_exc(file=open('badly.exc', 'w'))

print('Bye!!!')
