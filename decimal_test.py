import decimal

d = decimal.Decimal('3.141')

print(d)


decimal.getcontext().prec = 2

d = decimal.Decimal('1.00') / decimal.Decimal('3.00')

print(d)


a = 1.3333333333333333

print('%e' % a)

print('%4.2f' % a)

print('{0:4.4f}'.format(a))


x = 1999 + 1.33

pay = decimal.Decimal(str(x))

print(pay)

