"""
classtree.py: Climb inheritance trees using namespace links,
displaying higher superclasses with indentation for height
"""


def classtree(cls, indent):
    print('.' * indent + cls.__name__)
    print('\n\tcls: ', cls)
    print('\tcls.__bases__: ', cls.__bases__, '\n')
    for supercls in cls.__bases__:
        print('supercls: ', supercls)
        classtree(supercls, indent+3)  # recursion


def instancetree(inst):
    print('Tree of class %s' % inst)
    print('Tree of class %s' % list(inst.__class__.__bases__))  # inst.__class__.__bases__ must be wrapped in a list
    # call in order not to throw an error because .__bases__ returns a tuple of objects and must be wrapped in a list.
    print('Tree of class %s' % inst.__class__.__name__)
    classtree(inst.__class__, 3)


def selftest():
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    class E:
        pass

    class F(D, E):
        pass

    instancetree(B())
    instancetree(F())

    print('\n', '**' * 10, ' Testing ', '**' * 10, '\n')

    i = F()
    print(i.__class__)
    print(i.__class__.__name__)
    print(i.__class__.__bases__)

    for a in i.__class__.__bases__:
        print(a.__name__)


if __name__ == '__main__':
    selftest()


