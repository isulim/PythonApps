"""
A GUI app with database of books (Tkinter and SQLite3).
Program stores book informations:
Title, Author, Year, ISBN

User can:
- view records
- search an entry
- add an entry
- update an entry
- delete an entry
"""

import tkinter
from App5_DesktopDB.backend import Database


bookshelf = Database("bookshelf.db")


class Window(object):

    def __init__(self, root):
        self.root = root
        self.root.wm_title("Bookshelf")
        self.window = tkinter.Frame(root)
        self.window.grid(padx=10, pady=10)
        

        # Labels
        self.label_title = tkinter.Label(self.window, text='Title')
        self.label_title.grid(row=0, column=0)

        self.label_author = tkinter.Label(self.window, text='Author')
        self.label_author.grid(row=0, column=2)

        self.label_year = tkinter.Label(self.window, text='Year')
        self.label_year.grid(row=1, column=0)

        self.label_isbn = tkinter.Label(self.window, text='ISBN')
        self.label_isbn.grid(row=1, column=2)


        # Entries
        self.title_text = tkinter.StringVar()
        self.entry_title=tkinter.Entry(self.window, 
                                       textvariable=self.title_text)
        self.entry_title.grid(row=0, column=1)

        self.author_text = tkinter.StringVar()
        self.entry_author=tkinter.Entry(self.window, 
                                        textvariable=self.author_text)
        self.entry_author.grid(row=0, column=3)

        self.year_text = tkinter.StringVar()
        self.entry_year=tkinter.Entry(self.window, textvariable=self.year_text)
        self.entry_year.grid(row=1, column=1)

        self.isbn_text = tkinter.StringVar()
        self.entry_isbn=tkinter.Entry(self.window, textvariable=self.isbn_text)
        self.entry_isbn.grid(row=1, column=3)


        # Listbox + Slidebars
        self.slideBarX = tkinter.Scrollbar(self.window, 
                                           orient=tkinter.HORIZONTAL)
        self.slideBarX.grid(row=8, column=0, columnspan=2, sticky='WE')

        self.slideBarY = tkinter.Scrollbar(self.window, 
                                           orient=tkinter.VERTICAL)
        self.slideBarY.grid(row=3, column=2, rowspan=5, sticky="NS")

        self.listBox = tkinter.Listbox(self.window, height=8, width=35)
        self.listBox.grid(row=2, column=0, columnspan=2, rowspan=8)

        self.listBox.configure(xscrollcommand=self.slideBarX.set, 
                               yscrollcommand=self.slideBarY.set)
        self.slideBarX.configure(command=self.listBox.xview)
        self.slideBarY.configure(command=self.listBox.yview)

        # Selecting row in Listbox
        self.listBox.bind('<<ListboxSelect>>', self.get_row)


        # Buttons
        self.button_view = tkinter.Button(self.window, text='View all', 
                                          width=12, command=self.view_command)
        self.button_view.grid(row=2, column=3)


        self.button_search = tkinter.Button(self.window, text='Search entry', 
                                            width=12, 
                                            command=self.search_command)
        self.button_search.grid(row=3, column=3)


        self.button_add = tkinter.Button(self.window, text='Add entry', 
                                         width=12, command=self.insert_command)
        self.button_add.grid(row=4, column=3)


        self.button_update = tkinter.Button(self.window, text='Update selected', 
                                            width=12, 
                                            command=self.update_command)
        self.button_update.grid(row=5, column=3)


        self.button_delete = tkinter.Button(self.window, text='Delete selected', 
                                            width=12, 
                                            command=self.delete_command)
        self.button_delete.grid(row=6, column=3)


        self.button_close = tkinter.Button(self.window, text='Close', width=12, 
                                            command=root.destroy)
        self.button_close.grid(row=7, column=3)



    def view_command(self):
        self.listBox.delete(0, tkinter.END)
        for row in bookshelf.view_all():
            self.listBox.insert(tkinter.END, row)


    def search_command(self):
        self.listBox.delete(0, tkinter.END)
        for row in bookshelf.search(self.title_text.get(), 
                                    self.author_text.get(), 
                                    self.year_text.get(), 
                                    self.isbn_text.get()):
            self.listBox.insert(tkinter.END, row)


    def insert_command(self):
        bookshelf.insert(self.title_text.get(), self.author_text.get(),
                    self.year_text.get(), self.isbn_text.get())
        self.view_command()        

    # Getting row in Listbox
    def get_row(self, event):
        try: 
            global selected
            index = self.listBox.curselection()[0]
            data = self.listBox.get(index)
            selected = data[0]

            # Fill entries with selected data
            self.entry_title.delete(0, tkinter.END)
            self.entry_title.insert(tkinter.END, data[1])

            self.entry_author.delete(0, tkinter.END)
            self.entry_author.insert(tkinter.END, data[2])

            self.entry_year.delete(0, tkinter.END)
            self.entry_year.insert(tkinter.END, data[3])

            self.entry_isbn.delete(0, tkinter.END)
            self.entry_isbn.insert(tkinter.END, data[4])
        
        except IndexError: # When listbox is empty
            pass

    def delete_command(self):
        bookshelf.delete(selected)
        self.view_command()


    def update_command(self):
        bookshelf.update(selected, self.title_text.get(), 
                         self.author_text.get(), self.year_text.get(), 
                         self.isbn_text.get())
        self.view_command()


root = tkinter.Tk()
Window(root)
root.mainloop()