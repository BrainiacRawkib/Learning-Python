from fractions import Fraction
from decimal import Decimal


x = Fraction('0.33')

print(x)


x = Fraction('0.24')


print(x)


x = Fraction('.5')


print(x)

a = 2.5

x = a.as_integer_ratio()

print(x, type(x))  # x has been converted to Fraction

z = Fraction(*a.as_integer_ratio())  # the as_integer_ratio() method is a float method that can convert float and
# decimal(if imported from its module) to (numerator, denominator). the *as_integer_ratio() makes the result normal
# numerator, denominator while the as_integer_ratio() makes it a numerator, denominator with brackets
# (like a fraction in tuple). Then the Fraction() method now converts the numerator and denominator to a fraction.


print(z, type(z))

i = Fraction(1, 3)

print(float(i))

x = Fraction.from_float(1.75)

print(x)

x = Fraction.from_decimal(Decimal('1.1459'))

print(x)


i = Decimal('23.46')

print(i.as_integer_ratio(), type(i))  # this results to a tuple of numbers(numerator, denominator)

print(*i.as_integer_ratio())  # this results to a integers(numerator, denominator) separated by whitespaces


i = 0.3333333333333


a = Fraction(*i.as_integer_ratio())

print(a.limit_denominator(10), type(i))  # the limit_denominator() is a Fraction method used to simplify the result to
# the closest fraction








