import time
import timer_test


def timer(func, *args):
    start = time.clock()
    for i in range(1000):
        func(*args)
    return time.clock() - start


x = timer(pow, 2, 10)

print(x)

x = timer(str.upper, 'spam')

print(x)


x = timer_test.total(1000, pow, 2, 1000)[0]

print(x)

x = timer_test.bestof(1000, str.upper, 'spam')

print(x)

x = timer_test.bestoftotal(50, timer_test.total, 1000, str.upper, 'spam')

print(x)

