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
import backend


def view_command():
    listBox.delete(0, tkinter.END)
    for row in backend.view_all():
        listBox.insert(tkinter.END, row)


def search_command():
    listBox.delete(0, tkinter.END)
    for row in backend.search(title_text.get(), author_text.get(), 
                              year_text.get(), isbn_text.get()):
        listBox.insert(tkinter.END, row)


def insert_command():
    backend.insert(title_text.get(), author_text.get(),
                  year_text.get(), isbn_text.get())
    view_command()        

# Getting row in Listbox
def get_row(event):
    try: 
        global selected
        index = listBox.curselection()[0]
        data = listBox.get(index)
        selected = data[0]

        # Fill entries with selected data
        entry_title.delete(0, tkinter.END)
        entry_title.insert(tkinter.END, data[1])

        entry_author.delete(0, tkinter.END)
        entry_author.insert(tkinter.END, data[2])

        entry_year.delete(0, tkinter.END)
        entry_year.insert(tkinter.END, data[3])

        entry_isbn.delete(0, tkinter.END)
        entry_isbn.insert(tkinter.END, data[4])
    
    except IndexError: # When listbox is empty
        pass

def delete_command():
    backend.delete(selected)
    view_command()


def update_command():
    backend.update(selected, title_text.get(), author_text.get(), 
                   year_text.get(), isbn_text.get())
    view_command()

root = tkinter.Tk()
root.wm_title("Bookshelf")
window = tkinter.Frame(root)
window.grid(padx=10, pady=10)


# Labels
label_title = tkinter.Label(window, text='Title')
label_title.grid(row=0, column=0)

label_author = tkinter.Label(window, text='Author')
label_author.grid(row=0, column=2)

label_year = tkinter.Label(window, text='Year')
label_year.grid(row=1, column=0)

label_isbn = tkinter.Label(window, text='ISBN')
label_isbn.grid(row=1, column=2)


# Entries
title_text = tkinter.StringVar()
entry_title=tkinter.Entry(window, textvariable=title_text)
entry_title.grid(row=0, column=1)

author_text = tkinter.StringVar()
entry_author=tkinter.Entry(window, textvariable=author_text)
entry_author.grid(row=0, column=3)

year_text = tkinter.StringVar()
entry_year=tkinter.Entry(window, textvariable=year_text)
entry_year.grid(row=1, column=1)

isbn_text = tkinter.StringVar()
entry_isbn=tkinter.Entry(window, textvariable=isbn_text)
entry_isbn.grid(row=1, column=3)


# Listbox + Slidebars
slideBarX = tkinter.Scrollbar(window, orient=tkinter.HORIZONTAL)
slideBarX.grid(row=8, column=0, columnspan=2, sticky='WE')

slideBarY = tkinter.Scrollbar(window, orient=tkinter.VERTICAL)
slideBarY.grid(row=3, column=2, rowspan=5, sticky="NS")

listBox = tkinter.Listbox(window, height=8, width=35)
listBox.grid(row=2, column=0, columnspan=2, rowspan=8)

listBox.configure(xscrollcommand=slideBarX.set, yscrollcommand=slideBarY.set)
slideBarX.configure(command=listBox.xview)
slideBarY.configure(command=listBox.yview)

# Selecting row in Listbox
listBox.bind('<<ListboxSelect>>', get_row)


# Buttons
button_view = tkinter.Button(window, text='View all', width=12, 
                                     command=view_command)
button_view.grid(row=2, column=3)

button_search = tkinter.Button(window, text='Search entry', width=12,
                                       command=search_command)
button_search.grid(row=3, column=3)

button_add = tkinter.Button(window, text='Add entry', width=12, 
                                    command=insert_command)
button_add.grid(row=4, column=3)

button_update = tkinter.Button(window, text='Update selected', width=12, 
                                       command=update_command)
button_update.grid(row=5, column=3)

button_delete = tkinter.Button(window, text='Delete selected', width=12, 
                                       command=delete_command)
button_delete.grid(row=6, column=3)

button_close = tkinter.Button(window, text='Close', width=12, 
                                      command=root.destroy)
button_close.grid(row=7, column=3)


backend.create_table()
root.mainloop()