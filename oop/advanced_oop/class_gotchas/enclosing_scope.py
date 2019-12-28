def generate(label):
    class Spam:
        count = 1

        def method(self):
            print('%s = %s' % (label, Spam.count))

    return Spam()


aclass = generate('Gotchas')

# i = aclass()

# aclass().method()

aclass.method()
