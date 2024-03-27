from tkinter import *
from tkinter import ttk

root = Tk()
root.title('aaaaa')
entry_1 = ttk.Entry()
entry_2 = ttk.Entry()
entry_1.pack()
entry_2.pack()


def plus():
    a = int(entry_1.get())
    b = int(entry_2.get())
    ans = ttk.Label(text=a + b)
    ans.pack()


def minus():
    a = int(entry_1.get())
    b = int(entry_2.get())
    ans = ttk.Label(text=a - b)
    ans.pack()


plus_btn = ttk.Button(text='+', command=plus)
minus_btn = ttk.Button(text='-', command=minus)
plus_btn.pack()
minus_btn.pack()


def calc():
    a = int(entry_1.get())
    ans = ttk.Label(text=a)
    ans.pack()


calc_btn = ttk.Button(text='=', command=calc)
calc_btn.pack()
root.mainloop()
