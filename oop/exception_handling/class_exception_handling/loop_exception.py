class ExitLoop(Exception):
    def __str__(self):
        return 'Exiting Loop...'


try:
    while True:
        while True:
            for i in range(10):
                if i > 6:
                    raise ExitLoop()
                print('loop3: %s' % i)
            # print('loop2...')
        # print('loop1...')
except ExitLoop as x:
    print(x)
print(i)


