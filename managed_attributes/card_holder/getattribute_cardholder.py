class CardHolder:
    acct_len = 8
    retire_age = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def __getattribute__(self, item):
        super_get = object.__getattribute__
        if item == 'acct':
            return super_get(self, 'acct')[:-3] + '***'
        elif item == 'remain':
            return super_get(self, 'retire_age') - super_get(self, 'age')
        else:
            return super_get(self, item)

    def __setattr__(self, key, value):
        if key == 'name':
            value = value.lower().replace(' ', '_')
        elif key == 'age':
            if value < 0 or value > 150:
                raise ValueError('Invalid Age')
        elif key == 'acct':
            value = value.replace('-', '')
            if len(value) != self.acct_len:
                raise TypeError('Invalid Acct Number.')
        elif key == 'remain':
            raise TypeError('Cannot set remain.')
        self.__dict__[key] = value

