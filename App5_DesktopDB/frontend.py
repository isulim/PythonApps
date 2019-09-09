"""
A program to store book informations:
Title, Author, Year, ISBN

User can:

View records
Search an entry
Add an entry
Update an entry
Delete an entry
Close
"""

import tkinter

window = tkinter.Tk()

l1 = tkinter.Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = tkinter.Label(window, text='Author')
l2.grid(row=0, column=2)

l3 = tkinter.Label(window, text='Year')
l3.grid(row=1, column=0)

l4 = tkinter.Label(window, text='ISBN')
l4.grid(row=1, column=2)

title_text = tkinter.StringVar()
e1=tkinter.Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = tkinter.StringVar()
e2=tkinter.Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)


year_text = tkinter.StringVar()
e3=tkinter.Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)


isbn_text = tkinter.StringVar()
e4=tkinter.Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = tkinter.Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, columnspan=2, rowspan=6)

sb1 = tkinter.Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = tkinter.Button(window, text='View all', width=12)
b1.grid(row=2, column=3)

b2 = tkinter.Button(window, text='Search entry', width=12)
b2.grid(row=3, column=3)

b3 = tkinter.Button(window, text='Add entry', width=12)
b3.grid(row=4, column=3)

b4 = tkinter.Button(window, text='Update selected', width=12)
b4.grid(row=5, column=3)

b5 = tkinter.Button(window, text='Delete selected', width=12)
b5.grid(row=6, column=3)

b6 = tkinter.Button(window, text='Close', width=12)
b6.grid(row=7, column=3)



window.mainloop()