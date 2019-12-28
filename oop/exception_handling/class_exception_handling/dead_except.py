def func():
    try:
        raise IndexError
    except ArithmeticError:
        print('Every Exception dies...')
    except IndexError:
        print('IndexError Caught...')


try:
    func()
except IndexError:
    print('All dead...')
