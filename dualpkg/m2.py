from . import m1
import dualpkg.m1


def somefunc():
    m1.somefunc()
    print('m2.somefunc')


if __name__ == '__main__':
    somefunc()