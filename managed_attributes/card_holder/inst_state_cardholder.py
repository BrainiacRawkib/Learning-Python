class Name:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        value = value.lower().replace(' ', '_')
        instance._name = value


class Age:
    def __get__(self, instance, owner):
        return instance._age

    def __set__(self, instance, value):
        if value < 0 or value > 150:
            raise ValueError('Invalid Age.')
        else:
            instance._age = value


class Acct:
    def __get__(self, instance, owner):
        return instance._acct[:-3] + '***'

    def __set__(self, instance, value):
        value = value.replace('-', '')
        if len(value) != instance.acct_len:
            raise TypeError('Invalid Acct Number.')
        else:
            instance._acct = value


class Remain:
    def __get__(self, instance, owner):
        return instance.retire_age - instance._age

    def __set__(self, instance, value):
        raise TypeError('Cannot set remain.')


class CardHolder:
    acct_len = 8
    retire_age = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    age = Age()
    name = Name()
    acct = Acct()
    remain = Remain()


def printholder(who):
    print(who.acct, who.name, who.age, who.remain, who.addr, sep=' / ')


if __name__ == '__main__':
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

