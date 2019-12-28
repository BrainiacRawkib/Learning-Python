def truth(x, y):
    if x > y:
        return False
    return True


def is_ascending(lst):
    for i in range(len(lst) - 1):
        print(i, lst[i], lst[i + 1], truth(lst[i], lst[i + 1]))
        if lst[i] > lst[i + 1]:
            return False
    return True


x = is_ascending([11, 22, 33, 44, 55, 66, 55, 44, 33, 22, 11])

print(x)
