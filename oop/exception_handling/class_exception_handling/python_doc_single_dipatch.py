from functools import singledispatch


# @singledispatch
def fun(arg, verbose=False):
    print(int(verbose))
    if verbose:
        print(int(verbose))
        return 'Let me just say', arg, verbose
    return arg, verbose


x = fun('creepy is')

print(x)
