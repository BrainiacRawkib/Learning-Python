class ListInherited:
    """
    Use dir() to collect both instance attrs and names inheriteed from its classes;
    Pytbon 3.x shows more names than 2.x because of the implied object superclass in
    the advance oop-style class model;  getattr() fetched inherited names not in self.__dict__;
    use __str__, not __repr__, or else this loops when printing bound methods!
    """

    def __attrnames(self):
        result = ''

        for attr in dir(self):
            if attr[:2] == '__' and attr[-2] == '__':
                result += '\t%s\n' % attr
            else:
                result += '\t%s=%s\n' % (attr, getattr(self, attr))
        return result

    def __attrnames2(self, indent=' '*4):
        result = 'Unders%s\n%s%%s\nOthers%s\n' % ('-' * 77, indent, '-' * 77)
        unders = []

        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                unders.append(attr)
            else:
                display = str(getattr(self, attr))[:83-(len(indent) + len(attr))]
                result += '%s%s=%s\n' % (indent, attr, display)
        return result % ', '.join(unders)

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (self.__class__.__name__, id(self), self.__attrnames2())


if __name__ == '__main__':
    from oop.inheritance.testmixin import tester
    tester(ListInherited)


