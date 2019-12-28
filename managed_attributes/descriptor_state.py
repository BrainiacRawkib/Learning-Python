class DescState:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print('Descriptor State fetch...')
        return self.value * 10

    def __set__(self, instance, value):
        print('Descriptor State Set...')
        self.value = value
        print('setting instance value to : ', self.value)


# Client Class
class CalcAttrs:
    x = DescState(2)
    y = 3

    def __init__(self):
        self.z = 4


obj = CalcAttrs()
print(obj.x, obj.y, obj.z)

obj.x = 5

CalcAttrs.y = 6  # obj.y = 6 won't affect obj2.y result but CalcAttr will affect it.
obj.z = 7

print(obj.x, obj.y, obj.z)

print('--'*20)

obj2 = CalcAttrs()  # x and y use shared data because of descriptor state
print(obj2.x, obj2.y, obj2.z)

