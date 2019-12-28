class Error(ArithmeticError):
    pass


try:
    raise Error()
except:
    import sys
    print(sys.exc_info()[0:3])
