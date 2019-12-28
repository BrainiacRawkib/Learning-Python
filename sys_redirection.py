import sys

temp = sys.stdout

sys.stdout = open('log.txt', 'a')

x = 'open'
y = 'close'
z = 'print'

print(x, y, z)

sys.stdout.close()

sys.stdout = temp

print('sys.stdout has been closed')
