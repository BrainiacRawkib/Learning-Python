class FormatError(Exception):
    pass


def parser():
    raise FormatError(42, 'spammer.txt')


try:
    parser()
except FormatError as x:
    print('Error at line {} in {}'.format(x.args[0], x.args[1]))

