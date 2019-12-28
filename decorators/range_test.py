def rangetest(**argcheck):
    def on_decorator(func):
        def on_call(*args, **kwargs):
            print(argcheck)
            # for check in argcheck:
            #     pass
            return func(*args)
        return on_call
    return on_decorator


@rangetest(a=(1, 5), c=(0.0, 1.0))
def func(a, b, c, d=12, e=13):
    print(a + b + c + d + e)


x = func(23, 4, 66)
