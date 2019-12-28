class Life:
    instance = 0

    def __init__(self, name='unknown'):
        Life.instance += 1
        print('Hello... ' + name, Life.instance)
        self.name = name

    def live(self):
        print(self.name)

    def __del__(self):
        print('Deleting... ' + self.name)

    def __str__(self):
        return self.name


brian = Life('Brian')
bob = Life('Bob')
# brian.live()

print(brian)
print(bob)  # it printed it's self.name before deleting it, coz __del__ destruct works last

