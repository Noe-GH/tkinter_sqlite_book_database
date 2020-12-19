import tkinter as tk
import desktop_database_backend

#Variables:
selected_book = ""


def selected_book_value(value):
    """
    Function that assigns a value to the global variable selected_book.
    """
    global selected_book
    selected_book = value


def get_book_selected(event):
    if len(screen.curselection()) > 0:
        selected_book_value(screen.selection_get()[0])

        # Erase from Entries:
        e_author.delete(0,tk.END)
        e_year.delete(0,tk.END)
        e_title.delete(0,tk.END)
        e_isbn.delete(0,tk.END)

        indice = screen.curselection()[0]
        book = screen.get(indice)

        # Insert to Entries:
        e_author.insert(tk.END, book[1])
        e_year.insert(tk.END, book[2])
        e_title.insert(tk.END, book[3])
        e_isbn.insert(tk.END, book[4])


def view_all():
    screen.delete(0, tk.END)
    selected_book_value('')
    for records in desktop_database_backend.view_records():
        screen.insert(tk.END, records)

def search():
    screen.delete(0,tk.END)
    selected_book_value('')
    for resultado in desktop_database_backend.search_record(e_author.get(), e_year.get(), e_title.get(), e_isbn.get()):
        screen.insert(tk.END, resultado)

def add_to_table():
    screen.delete(0, tk.END)
    selected_book_value('')
    if e_author.get() != "" and e_year.get() != "" and e_title.get() != "" and e_isbn.get() != "":
        desktop_database_backend.add_record(e_author.get(), e_year.get(), e_title.get(), e_isbn.get())
        screen.insert(tk.END, 'Book added.')
    else:
        screen.insert(tk.END, 'Please, fill every field')

def update_in_table():
    global selected_book
    if selected_book != "":
        #print('\n\n\n',e_author.get(), e_year.get(), e_title.get(), e_isbn.get(), '\n\n\n')
        desktop_database_backend.update_record(selected_book, e_author.get(), e_year.get(), e_title.get(), e_isbn.get())        
        screen.delete(0, tk.END)
        screen.insert(tk.END, 'Book updated')
    else:
        screen.delete(0, tk.END)
        screen.insert(tk.END, 'Select a book')

def delete_from_table():
    global selected_book
    if selected_book != "":
        screen.delete(0, tk.END)        
        desktop_database_backend.delete_record(selected_book)
        screen.insert(tk.END, 'Book deleted')
    else:
        screen.delete(0, tk.END)
        screen.insert(tk.END, 'Select a book')


v = tk.Tk()

v.wm_title('Book database')

# Create widgets: --------------------------------
lbl_title = tk.Label(text='Title: ')
e_title = tk.Entry()
lbl_author = tk.Label(text='Author: ')
e_author = tk.Entry()
lbl_year = tk.Label(text='Year: ')
e_year = tk.Entry()
lbl_isbn = tk.Label(text='ISBN: ')
e_isbn = tk.Entry()

screen = tk.Listbox(height=7, width=35)
sb = tk.Scrollbar()
screen.configure(yscrollcommand=sb)
sb.configure(command=screen.yview)

screen.bind('<<ListboxSelect>>', get_book_selected)

btn_see_all = tk.Button(text='See all', width=16, command=view_all)
btn_search = tk.Button(text='Search', width=16, command=search)
btn_add = tk.Button(text='Add', width=16, command=add_to_table)
btn_update = tk.Button(text='Update', width=16, command=update_in_table)
btn_erase = tk.Button(text='Erase selected', width=16, command=delete_from_table)
btn_close = tk.Button(text='Close', width=16, command=v.destroy)


# Place widgets: ------------------------------
lbl_title.grid(row=0, column=0)
e_title.grid(row=0, column=1, padx=2, pady=3)
lbl_author.grid(row=0, column=2)
e_author.grid(row=0, column=3, padx=2, pady=3)
lbl_year.grid(row=1, column=0)
e_year.grid(row=1, column=1, padx=2, pady=3)
lbl_isbn.grid(row=1, column=2)
e_isbn.grid(row=1, column=3, padx=2, pady=3)

sb.grid(row=3, column=2, rowspan=4)

btn_see_all.grid(row=2, column=3, pady=3)
screen.grid(row=3, column=0, rowspan=4, columnspan=2, padx=5)
btn_search.grid(row=3, column=3, pady=3)
btn_add.grid(row=4, column=3, pady=3)
btn_update.grid(row=5, column=3, pady=3)
btn_erase.grid(row=6, column=3, pady=3)
btn_close.grid(row=7, column=3, pady=3)


v.mainloop()




