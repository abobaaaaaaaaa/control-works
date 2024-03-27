from tkinter import *
import random

a = random.randint(1, 700)
b = random.randint(1, 700)
root = Tk()
root.title('aaaaa')
root.geometry('1280x720')
canvas = Canvas(bg="white", width=1200, height=700)
canvas.pack(anchor=CENTER, expand=1)
def oval(canvas):
    canvas.create_oval(a, b, a + 10, b + 10)
root.bind('<Button-1>',oval(canvas))
root.mainloop()
