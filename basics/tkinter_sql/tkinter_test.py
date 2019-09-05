from tkinter import *

window = Tk()

def kgConvert():
    kgsToGrams = float(e1_value.get()) * 1000
    kgsToLbs = round((float(e1_value.get()) * 2.204062), 4)
    kgsToOz = round((float(e1_value.get()) * 35.274), 4)
    t1.delete(1.0, END)
    t2.delete(1.0, END)
    t3.delete(1.0, END)
    t1.insert(END, kgsToGrams)
    t2.insert(END, kgsToLbs)
    t3.insert(END, kgsToOz)

l0 = Label(window, text="Kg")
l0.grid(row=0, column=0, columnspan=1)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value, width=40)
e1.grid(row=0, column=1, columnspan=3)

b1 = Button(window, text="Convert", command=kgConvert, width=30, height=1)
b1.grid(row=0, column=4, columnspan=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=1)
l1 = Label(window, text="grams")
l1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=3)
l2 = Label(window, text="lbs")
l2.grid(row=1, column=2)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=5)
l3 = Label(window, text="oz")
l3.grid(row=1, column=4)

window.mainloop()
