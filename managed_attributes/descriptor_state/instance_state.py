class InstanceState:
    def __get__(self, instance, owner):
        print('Instance State get...', self.__class__.__name__, instance.__class__.__name__)
        return instance._x * 10, instance.z

    def __set__(self, instance, value):
        print('Instance State set...')
        instance._x = value
        instance.z = value
        print("setting instances' values to : ", instance._x, instance.z)


# Client class
class CalcAttrs:
    x = InstanceState()  # instance state
    y = 3

    def __init__(self):
        self._x = 2
        self.z = 4


obj = CalcAttrs()
obj2 = CalcAttrs()

print(obj.x, obj.y, obj.z)

obj.x = 5

CalcAttrs.y = 6  # this line will affect obj2.y result because CalcAttr is obj2 class

obj.z = 7
print(obj.x, obj.y, obj.z)

print(obj2.x, obj2.y, obj2.z)

