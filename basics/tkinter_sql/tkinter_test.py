from tkinter import *

window = Tk()

def milesToKm():
    kms = round((float(e1_value.get()) * 1.6), 2)
    t1.delete(1.0, END)
    t1.insert(END, kms) # insert at the end


b1 = Button(window, text="Execute", command=milesToKm)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()
