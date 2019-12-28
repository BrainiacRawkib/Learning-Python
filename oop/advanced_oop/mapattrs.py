"""
File mapattrs.py (3.x + 2.x)

Main tool: mapattrs() maps all attributes on or inherited by an
instance to the instance or class from which they are inherited.

Assumes dir() gives all attributes of an instance. To simulate inheritance,
uses either the class's MRO tuple, which gives the search order for advance oop-style
classes (and all in 3.x), or a recursive traversal to infer the DFLR order of classic
classes in 2.x.

Also here: inheritance() gives version-neutral class ordering; assorted
dictionary tools using 3.x/2.7 comprehensions.
"""

import pprint


def trace(x, label='', end='\n'):
    print(label + pprint.pformat(x) + end)


def filterdictvals(d, v):
    """
    dict D with entries for value v removed.
    filterdictvals (dict(a=1, b=2, c=1), 1) => {'b'}: 2
    """
    return {k: v2 for (k, v2) in d.items() if v2 != v}


def invertdict(d):
    """
    dict d with values changed to keys (grouped by values).
    Values must all be hashable to work as dict/set keys.
    invertdict(dict(a=1, b=2, c=1)) => {1: ['a', 'c'], 2: ['b']}
    """

    def keysof(v):
        return sorted(k for k in d.keys() if d[k] == v)
    return {v: keysof(v) for v in set(d.values())}


def dflr(cls):
    """
    Classis depth-first left-to-right order of class tree at cls.
    Cycles not possible: Python disallows on __bases__ changes.
    """
    here = [cls]

    for sup in cls.__bases__:
        here += dflr(sup)
    return here


def inheritance(instance):
    """
    Inheritance order sequence: advance oop-style (MRO) or classic (DFLR)
    """
    if hasattr(instance.__class__, '__mro__'):
        return (instance,) + instance.__class__.__mro__
    else:
        return [instance] + dflr(instance.__class__)


def mapattrs(instance, withobject=False, bysource=False):
    """
    dict with keys giving all inherited attributes of instance,
    with values giving the object that each is inherited from.
    withobject: False=remove object built-in class attributes.
    bysource: True=group result by objects instead of attributes.
    Supports classes with slots that preclude __dict__ in instances.
    """
    attr2obj = {}
    inherits = inheritance(instance)
    for attr in dir(instance):
        for obj in inherits:
            if hasattr(obj, '__dict__') and attr in obj.__dict__:  # See slots
                attr2obj[attr] = obj
                break

    if not withobject:
        attr2obj = filterdictvals(attr2obj, object)
    return attr2obj if not bysource else invertdict(attr2obj)


if __name__ == '__main__':
    print('Classic classes in 2.x, advance oop-style in 3.x')

    class A:
        attr1 = 1

    class B(A):
        attr2 = 2

    class C(A):
        attr1 = 3

    class D(B, C):
        pass

    i = D()

    print('Py=>%s' % i.attr1)

    trace(inheritance(i),       'INH\n')
    trace(mapattrs(i),      'ATTRS\n')
    trace(mapattrs(i, bysource=True), 'OBJS\n')

    print('New-style classes in 2.x and 3.x')

    class A(object):
        attr1 = 1

    class B(A):
        attr2 = 2

    class C(A):
        attr1 = 3

    class D(B, C):
        pass

    i = D()
    print('Py=>%s' % i.attr1)
    trace(inheritance(i),       'INH\n')
    trace(mapattrs(i),          'ATTRS\n')
    trace(mapattrs(i, bysource=True), 'OBJS\n')




