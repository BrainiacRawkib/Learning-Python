print('%(qty)d more %(food)s' % {'qty': 10, 'food': 'spam'})


reply = """
Greetings...
Hello %(name)s!.
Your age is %(age)d
"""

values = {'name': 'Bob', 'age': 40}

print(reply % values)

qty = 20
food = 'bags of rice'

x = '%(qty)d more %(food)s' % vars()

print(x)

c = '{motto}, {pork} and {food}'.format(motto='spam', pork='ham', food='eggs')

print(c)

import sys

x = 'My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})

print(x)

x = 'My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'})

print(x)

somelist = list('SPAM')

newlist = list('RAMPS')

x = 'first={0[0]}, third={0[2]}, first={1[0]}, second={1[1]}, fourth={1[3]}'.format(somelist, newlist)

print(x)

x = 'first={0}, last={1}'.format(somelist[0], somelist[-1])

print(x)

parts = somelist[0], somelist[-1], somelist[1:3]

x = 'first={0}, last={1}, middle={2}'.format(*parts)

print(x)

x = '{0:10} = {1:10}'.format('spam', 123.4567)

print(x)

x = '{0:>10} = {1:<10}'.format('spam', 123.4567)

print(x)

x = '{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop'))

print(x)

x = '{.platform:>10} = {[kind]:<10}'.format(sys, dict(kind='laptop'))

print(x)

x = '{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159)

print(x)

x = '{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159)

print(x)

x = '{0:x}, {1:o}, {2:b}'.format(255, 255, 255)

print(x)

x = '{0}, {1}'.format(3.14, [1, 2])

print(x)

data = dict(platform=sys.platform, kind='laptop')

x = 'My {kind:<8} runs {platform:>8}'.format(**data)

print(x)

x = 'My %(kind)-8s runs %(platform)8s' % data

print(x)

x = '{0:,.2f}'.format(999999999.0232)

print(x)

x = '{0:,.2f}'.format(999999999)

print(x)

x = '{0:,d}'.format(999999999)

print(x)

x = '{:,d}, {:,d}'.format(999999999, 8888888)

print(x)

x = '{name} {job} {name}'.format(name='Brain', job='Dev')

print(x)

x = '%(name)s %(job)s %(name)s' % dict(name='Brain', job='Hacker')

print(x)

d = dict(name='Bob', job='M.D')

x = '{0[name]} {0[job]} {0[name]}'.format(d)

print(x)

x = '{name} {job} {name}'.format(**d)

print(x)





