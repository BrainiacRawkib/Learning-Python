import time


def timer(label='', trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.clock()
            result = self.func(*args, **kwargs)
            elapsed = time.clock() - start
            self.alltime += elapsed

            if trace:
                _format = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(_format % values)
            return result
    return Timer


if __name__ == '__main__':
    import sys
    force = list if sys.version_info[0] == 3 else (lambda x: x)

    @timer(label='[CCC]===>')
    def list_comp(n):
        return [x * 2 for x in range(n)]

    @timer(label='[MMM]===>')
    def map_call(n):
        return force(map((lambda x: x * 2), range(n)))


    for func in (list_comp, map_call):
        result = func(5)
        func(50000)
        func(500000)
        func(1000000)
        print(result)
        print('AllTime = %s\n' % func.alltime)

    print('**map/comp = %s' % round(map_call.alltime / list_comp.alltime, 3))
