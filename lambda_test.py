def func():
    x = 4
    action = lambda n: x ** n
    return action


x = func()

print(x(2))


def make_actions():
    """
    any nested function (def or lambda) inside a loop (for or while) should explicitly default the inner variable to the
    outer one in order to keep track of the current value of of the outer variable,just as we done here.
    Because defaults are evaluated when the nested function is created (not when it’s later called), each remembers its
    own value for i:
    :return:
    """
    acts = []
    for i in range(5):
        acts.append(lambda x, a=i: a ** x)
    return acts


f = make_actions()

print(f[0](2))  # 0 reps index for the for loop in the make_actions() while 2 reps the power x in lambda x, a=i: a ** x
print(f[1](2))  # that's why index came before the power.
print(f[2](2))
print(f[3](2))
print(f[4](2))


def makeaction():
    acts = []
    i = 0
    while i < 5:
        acts.append(lambda x, i=i: i ** x)

        i += 1
    return acts


x = makeaction()

print(x[0](2))
print(x[1](2))
print(x[2](2))
print(x[3](2))
print(x[4](2))
# print(x[5](2))  # out of range (Index Error)

