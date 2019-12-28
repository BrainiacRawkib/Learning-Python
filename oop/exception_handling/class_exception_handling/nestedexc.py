def action2():
    print(1 + [])  # Generate TypeError


def action1():
    try:
        action2()
    except TypeError:
        print('action2 try.')


try:
    action1()
except TypeError:
    print('action1 try.')


try:
    try:
        action2()
    except TypeError:
        print('inner try exception.')
except TypeError:
    print('outer try exception.')


try:
    raise ArithmeticError()
except Exception:
    print('ArithmeticError Caught.')

