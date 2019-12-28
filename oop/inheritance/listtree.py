class ListTree:
    """
    Mix-in that returns an __str__ trace of the entire class tree and all
    its objects' attrs at and above self; run by print(), str() returns
    constructed string; uses __X attr names to avoid impacting clients;
    recurses to superclasses explicitly, uses str.format() for clarity;
    """

    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result

    def __listclass(self, aklass, indent):
        dots = '.' * indent
        if aklass in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(dots, aklass.__name__, id(aklass))
        else:
            self.__visited[aklass] = True
            here = self.__attrnames(aklass, indent)
            above = ''
            for super in aklass.__bases__:
                above += self.__listclass(super, indent+4)
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(dots,
                                                                        aklass.__name__,
                                                                        id(aklass),
                                                                        here, above, dots)

    def __str__(self):
        self.__visited = {}
        here = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(self.__class__.__name__,
                                                                id(self),
                                                                here, above)


if __name__ == '__main__':
    from oop.inheritance.testmixin import tester
    tester(ListTree)

