class GetAttr:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, attr):  # on undefined attrs fetches only
        print('getattr: ' + attr)
        if attr == 'attr3':
            return 3
        else:
            raise AttributeError(attr)


x = GetAttr()
print(x.attr1)
print(x.attr2)
print(x.attr3)

print('--'*20)


class GetAttribute(object):
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattribute__(self, item):  # on all attr fetches
        print('getattribute: ' + item)
        if item == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, item)  # for defined attr


x = GetAttribute()
print(x.attr1)
print(x.attr2)
print(x.attr3)

