import sys
from tkinter import Button, mainloop


x = Button(text="Click!", command=(lambda: sys.stdout.write('Spam Detected!\n')))
x.pack()

mainloop()


