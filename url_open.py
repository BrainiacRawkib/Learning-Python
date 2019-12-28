from urllib.request import urlopen


for line in urlopen('http://home.rmi.net/~lutz'):
    print(line)
