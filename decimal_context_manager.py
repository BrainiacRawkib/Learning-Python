import decimal
from decimal import Decimal


x = Decimal('1.00') / Decimal('3.00')

print(x)


with decimal.localcontext() as ctx:  # decimal.localcontext() is for local precision setting while decimal.getcontext().prec is for global precision setting
    ctx.prec = 3
    x = Decimal('1.009') / Decimal('3.00')
    print(x)

x = Decimal('1.00') / Decimal('3.00')

print(x)


def decimal_ctx(a, s):
    with decimal.localcontext() as ctx:
        ctx.prec = 4

        x = Decimal(a) / Decimal(s)
        print(x)


decimal_ctx(12.00, 34.99)
