class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        print('Meeting property setter...')
        value = value.lower().replace(' ', '_')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0 or value > 150:
            raise ValueError('Invalid Age.')
        else:
            self.__age = value

    @property
    def acct(self):
        return self.__acct[:-3] + '***'

    @acct.setter
    def acct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('Invalid Acct Number.')
        else:
            self.__acct = value

    @property
    def remain(self):
        return self.retireage - self.age


# def load_class():
#     import sys, importlib
#     module_name = sys.argv[1]
#     module = importlib.import_module(module_name)
#     print('[Using: %s]' % module.CardHolder)
#     return module.CardHolder


def printholder(who):
    print(who.acct, who.name, who.age, who.remain, who.addr, sep=' / ')


if __name__ == '__main__':
    # CardHolder = load_class()
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    printholder(bob)

    bob.name = 'Bob Q.Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    printholder(bob)

    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    printholder(sue)

    try:
        sue.age = 200
    except:
        print('Bad age for sue.')

    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")

    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for sue')

