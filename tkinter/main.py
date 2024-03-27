from tkinter import *
from tkinter import ttk
root=Tk()
root.title('aaaaa')
def enter(arg):
    label=ttk.Label(text='hello world')
    label.pack()
root.bind('<Return>',enter)

root.mainloop()