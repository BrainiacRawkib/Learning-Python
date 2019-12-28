import os

f = os.popen('dir')
x = f.readline()

print(x)

f = os.popen('dir')
x = f.read(50)

print(x)

f = os.popen('dir').readlines()[0]

print(f)

f = os.popen('dir').read()[:50]

print(f)

for line in os.popen('dir'):
    print(line.rstrip())



