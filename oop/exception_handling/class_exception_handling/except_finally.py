def raise1():
    raise IndexError()


def no_raise():
    return


def raise2():
    raise SyntaxError()


for func in raise1, no_raise, raise2:
    print('\n***** <%s> *****\n' % func.__name__)

    try:
        func()
    except IndexError:
        print('Caught IndexError Exception.')
    except SyntaxError:
        print('Caught SyntaxError Exception.')
    else:
        print('No Exception Raised.')
    finally:
        print('Finally run.')
    print('Finished...')


