x = 1


def nester():
    x = 2
    print('nester: ', x)

    class C:
        x = 3
        print('C: ', x)

        def method1(self):
            print(x)  # it prints 2 in the enclosing def not 3 in class C:
            print(self.x)  # it prints 3 in the class C:

        def method2(self):
            x = 4
            print(x)
            self.x = 5
            print(self.x)

    i = C()
    i.method1()
    i.method2()


print('first global: ', x)
nester()
print('-' * 40)

