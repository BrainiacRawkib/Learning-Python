x, y, z = 43, 44, 45

s = 'SPAM'

d = {'a': 1, 'b': 2}

l = [1, 2, 3]


f = open('datafile.txt', 'w')
f.write(s + '\n')
f.write('%s,%s,%s\n' % (x, y, z))
f.write(str(l) + '$' + str(d) + '\n')
f.close()

chars = open('datafile.txt')

f = chars.readline()

print(f.rstrip())

f = chars.readline().rstrip().split(',')

print([int(x) for x in f])

f = chars.readline().rstrip().split('$')

print(f)

objects = [eval(x) for x in f]

print(objects)


import pickle


d = {'a': 1, 'b': 2}

f = open('datafile.pkl', 'wb')

pickle.dump(d, f)  # pickle any object to file

f.close()

f = open('datafile.pkl', 'rb')

x = pickle.load(f)  # load any object from file

print(x)


i = open('datafile.pkl', 'rb').read()

print(i)


