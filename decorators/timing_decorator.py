import time, sys


force = list if sys.version[0] == 3 else (lambda x: x)
print(sys.version)


class Timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0

    def __call__(self, *args, **kwargs):
        start = time.clock()
        result = self.func(*args, **kwargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result


@Timer
def list_comp(n):
    return [x * 2 for x in range(n)]


@Timer
def map_call(n):
    return force(map((lambda x: x * 2), range(n)))


result = list_comp(5)
list_comp(50000)
list_comp(500000)
list_comp(1000000)

print(result)
print('AllTime = %s' % list_comp.alltime)


print('')
result = map_call(5)
map_call(50000)
map_call(500000)
map_call(1000000)
print(list(result))
print('AllTime = %s' % map_call.alltime)

print('\n**map/comp = %s' % round(map_call.alltime / list_comp.alltime, 3))
