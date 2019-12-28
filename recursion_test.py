def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        print('L[0] : ', L[0])
        return L[0] + mysum(L[1:])  # Direct recursion


print(mysum([1, 2, 3, 4, 5]))


def mysum2(L):
    return 0 if not L else L[0] + mysum2(L[1:])


print(mysum2([1, 2, 3, 4, 5]))


def mysum3(L):
    return L[0] if len(L) == 1 else L[0] + mysum3(L[1:])


print(mysum3(('s', 'p', 'a', 'm')))


def mysumm(L):
    if not L:
        return 0
    return nonempty(L)  # Calls a function that calls me


def nonempty(L):
    return L[0] + mysumm(L[1:])  # Indirectly recursive


print(mysumm([1.1, 2.2, 3.3, 4.4]))


def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot


L = [1, [2, [3, 4], 5], 6, [7, 8]]

print(sumtree(L))
print(sumtree([1, [2, [3, [4, [5]]]]]))


print('\n\n', '*' * 30, '\n\n')


def sumtree2(L):  # Breadth-first, explicit queue
    tot = 0
    items = list(L)
    while items:
        print('items : ', items)
        front = items.pop(0)
        print('front : ', front)
        if not isinstance(front, list):
            tot += front  # add numbers directly
            print('tot : ', tot, '\n')
        else:
            items.extend(front)  # append all in nested list
    return tot


print(sumtree2([1, [2, [3, [4, [5]]]]]))


print('\n\n', '*' * 30, '\n\n')


def sumtree3(L):  # Depth-first, explicit stack
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front  # add numbers directly
        else:
            items[:0] = front
    return tot  # prepend all in nested list


print(sumtree3([1, [2, [3, [4, [5]]]]]))


import sys

print(sys.getrecursionlimit())


print('\n\n', '*' * 30, '\n\n')


print(sumtree.__code__.co_argcount)
print(sumtree.__code__.co_varnames)
print(sumtree.__code__.co_filename)


