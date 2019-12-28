class Descriptor:
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')


class Subject:
    attr = Descriptor()


x = Subject()
x.attr

print('-'*40)

Subject.attr
