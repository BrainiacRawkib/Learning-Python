from oop.person import Person


bob = Person('bob smith')

print(bob)


print(bob.__class__.__name__)

x = list(bob.__dict__.keys())

print(x)

x = bob.__dict__

print(x)

for key in bob.__dict__:
    print(key, '-->', bob.__dict__[key])


for key in bob.__dict__:
    print(key, '-->', getattr(bob, key))

