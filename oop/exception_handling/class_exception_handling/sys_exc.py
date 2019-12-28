import sys


def bye():
    sys.exit(40)


try:
    bye()
except:
    print('Got all exceptions...')
else:
    print('Not exception occurred...')
print('continuing...')



