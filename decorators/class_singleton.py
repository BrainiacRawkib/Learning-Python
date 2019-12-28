# instances = {}

# 2.x and 3.x only


# def singleton(aClass):  # On @ decoration
#     instances = {}
#
#     def onCall(*args, **kwargs):                # On instance creation
#         if aClass not in instances:             # One dict entry per class
#             instances[aClass] = aClass(*args, **kwargs)
#             print(instances.keys(), instances.values())
#         return instances[aClass]
#     return onCall


# 3.x only
# def singleton(aklass):
#     instance = None
#
#     def oncall(*args, **kwargs):
#         nonlocal instance
#         if instance == None:
#             instance = aklass(*args, **kwargs)
#         return instance
#     return oncall


# 3.x and 2.x
# def singleton(klass):
#     def oncall(*args, **kwargs):
#         if oncall.instance == None:
#             oncall.instance = klass(*args, **kwargs)
#         return oncall.instance
#     oncall.instance = None
#     return oncall


class singleton:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance


@singleton
class Person:
    def __init__(self, name, hours, rate, job=None):
        self.name = name
        self.hours = hours
        self.rate = rate
        self.job = job

    def pay(self):
        return self.hours * self.rate


@singleton
class Spam:
    def __init__(self, val):
        self.attr = val


bob = Person('Bob', 40, 10, 'Mgr')
print(bob.name, bob.pay(), bob.job)

spam = Spam(30)
print(spam.attr)

