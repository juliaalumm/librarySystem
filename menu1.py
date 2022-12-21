from tkinter import *
from tkinter import ttk
from bookrecommend import bookrecommend
from bookreturn import book_return
from bookcheckout import book_checkout
from booksearch import book_search


#this for the tabs so that when you select a button on the main menu itll direct you to a tab
def select_search():
    my_notebook.select(1)

def select_checkout():
    my_notebook.select(2)

def select_return():
    my_notebook.select(3)

def select_reco():
    my_notebook.select(4)

root = Tk()
root.title("Library Management System")

my_notebook = ttk.Notebook(root)
my_notebook.pack()

#the tabs
menu_tab = Frame(my_notebook, width = 1000, height = 1000)
book_search_tab = Frame(my_notebook, width = 1000, height = 1000)
book_checkout_tab = Frame(my_notebook, width = 1000, height = 1000)
book_return_tab = Frame(my_notebook, width = 1000, height = 1000)
book_recommend_tab = Frame(my_notebook, width = 1000, height = 1000)

menu_tab.pack(fill="both",expand = 1)
book_search_tab.pack(fill="both", expand = 1)
book_checkout_tab.pack(fill="both", expand = 1)
book_return_tab.pack(fill="both", expand = 1)
book_recommend_tab.pack(fill="both", expand = 1)

my_notebook.add(menu_tab, text="Main Menu")
my_notebook.add(book_search_tab, text="Search For A Book")
my_notebook.add(book_checkout_tab, text="Checkout A Book")
my_notebook.add(book_return_tab, text="Return A Book")
my_notebook.add(book_recommend_tab, text="Get Recommended A Book")

#MAIN MENU TAB

title = Label(menu_tab, text = "Welcome to the Library", font = ("Arial",60))
title.config(anchor=CENTER)
title.pack(pady = 50, padx = 150)

services = Label(menu_tab, text = "Select a service", font = ("Arial",40))
services.config(anchor = CENTER)
services.pack(pady = (0,50))

#buttons to go to their respective tabs
main_search = Button(menu_tab, text= "Search for a book",command = select_search, font=("Arial",20))
main_search.config(anchor = CENTER)
main_search.pack(pady = (0,30))

main_checkout = Button(menu_tab, text= "Checkout a book",command = select_checkout, font=("Arial",20))
main_checkout.config(anchor = CENTER)
main_checkout.pack(pady = (0,30))

main_return = Button(menu_tab, text= "Return a book",command = select_return, font=("Arial",20))
main_return.config(anchor = CENTER)
main_return.pack(pady = (0,30))

main_recommend = Button(menu_tab, text= "Get recommended a book",command = select_reco, font=("Arial",20))
main_recommend.config(anchor = CENTER)
main_recommend.pack(pady = (0,50))

#SEARCH TAB

search_title= Label (book_search_tab, text = "Search For A Book", font = ("Arial",40))
search_title.config(anchor = CENTER)
search_title.pack(pady = 40 )

#entry box for book search
search_M1 = Label (book_search_tab, text = "Enter A Book Title:", font = ("Arial", 20)).pack()
search_entry = Entry(book_search_tab, font = ("Helvetica", 20))
search_entry.pack()

#button to call booksearch function
search_button = Button(book_search_tab, text = "Search", font = ("Arial", 15),
                       command = lambda:  book_search(book_search_tab,search_entry.get()))
search_button.pack(pady = 20)


#CHECKOUT TAB

search_checkout= Label (book_checkout_tab, text = "Checkout A Book", font = ("Arial",40))
search_checkout.config(anchor = CENTER)
search_checkout.pack(pady = 40)

#entry box for book checkout Member ID
checkout_M1 = Label (book_checkout_tab, text = "Member ID:", font = ("Arial", 20)).pack()
checkout1_entry = Entry(book_checkout_tab, font = ("Helvetica", 20))
checkout1_entry.pack()

#entry box for book checkout Book ID
checkout_M2 = Label (book_checkout_tab, text = "Book ID:", font = ("Arial", 20)).pack()
checkout2_entry = Entry(book_checkout_tab, font = ("Helvetica", 20))
checkout2_entry.pack()

#button to call bookcheckout function
checkout_button = Button(book_checkout_tab, text = "Enter", font = ("Arial", 15),
                  command = lambda: book_checkout(book_checkout_tab,checkout1_entry.get(),checkout2_entry.get()))
checkout_button.pack(pady = 20)

#RETURN TAB

search_return= Label (book_return_tab, text = "Return A Book", font = ("Arial",40))
search_return.config(anchor = CENTER)
search_return.pack(pady = 40 )

#entry box for book return
return_M1 = Label (book_return_tab, text = "Book ID:", font = ("Arial", 20)).pack()
return_entry = Entry(book_return_tab, font = ("Helvetica", 20))
return_entry.pack()

#button to call bookreturn function
return_button = Button(book_return_tab, text = "Enter", font = ("Arial", 15),
                       command = lambda : book_return(book_return_tab,return_entry.get()))
return_button.pack(pady = 20)


#RECOMMEND TAB

search_reco = Label (book_recommend_tab, text = "Get Recommended A Book", font = ("Arial",40))
search_reco.config(anchor = CENTER)
search_reco.pack(pady = 40)

#entry box for book recommend
reco_M1 = Label (book_recommend_tab, text = "Enter Your Member ID:", font = ("Arial", 20)).pack()
reco_entry = Entry(book_recommend_tab, font = ("Helvetica", 20))
reco_entry.pack()

#button to call bookrecommend function
reco_button = Button(book_recommend_tab, text = "Search", font = ("Arial", 15),
                     command = lambda:bookrecommend(book_recommend_tab,reco_entry.get()))
reco_button.pack(pady = 20)

root.mainloop()
