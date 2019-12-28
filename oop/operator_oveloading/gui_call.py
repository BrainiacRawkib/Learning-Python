from tkinter import Button


class CallBack:
    def __init__(self, color):
        self.color = color

    def __call__(self):
        print('turn', self.color)


cb1 = CallBack('blue')
cb2 = CallBack('green')

B1 = Button(command=cb1)
B2 = Button(command=cb2)

cb1()
cb2()


def callback(color):
    def oncall():
        return ''.join(('turn ', color))
    return oncall()


cb3 = callback('yellow')
print(cb3)

cb4 = callback('red')
print(cb4)



