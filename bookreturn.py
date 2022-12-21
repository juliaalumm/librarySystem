from datetime import datetime
from datetime import date
from database import *
from tkinter import *

logfile = []
database = []
lines =[]

def book_return(book_return_tab,bookID):

    """
    F119883
    16 December 2021
    :param book_return_tab:
    :param bookID:
    :return:
    this function edits the logfile and database to let the user return the book
    """

    #opens the logfile.txt and database.txt
    database_open(database)
    logfile_open(logfile)

    for i in database:
        #checks if the book is already checked out and also if the bookID matched the one in the database
        if i[5] != "0" and i[0] == bookID:
            #changes the memberID value to 0 so that it can be seen and read as available and lets the user know
            i[5] = '0'
            l1 = Label(book_return_tab, text = "Book Return Successful", font = ("Arial", 30, "bold"), fg = "#6aa84f").pack(pady= (0,20))
            break
        #checks if the bookID matches the one in the database and if the book is already available and lets the user know
        elif bookID == i[0] and i[5] == "0":
            l2 = Label(book_return_tab, text = "Book is already available", font = ("Arial",20)).pack()
            break
    #if all of the other criteria doesnt fir the last resort would be that the bookID is invalid and it lets the user know
    else:
        l3 = Label(book_return_tab, text="Book ID Invalid", font=("Arial", 20)).pack()

    #gets the date today and for line 42 i needed to change the format to be able to get the century into it
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    today = today[:6] + '20'+today[-2:]
    for l in logfile:
        if bookID == l[0]:
            if l[2] == "0":
                #finding the diffference between the date it was checked out and today
                date_format = "%d/%m/%Y"
                a = datetime.strptime(l[1], date_format)
                b = datetime.strptime(today, date_format)
                delta = b - a
                dayDiff = delta.days
                #checks if the book has been checked out for more than 60 days and also that the bookID matches and its also available and changes the logfile to todays date
                if dayDiff >= 60 and bookID == l[0] and l[2] == "0":
                    l4 = Label(book_return_tab, text = "Book has been checked out for "+str(dayDiff)+" days.", font= ("Arial",20), fg = "red").pack()
                    l[2] = str(today)
                #if the book hasnt been checked out for more than 60 days so it just changes the logfile to todays date
                elif bookID == l[0] and l[2] == "0":
                    l[2] = str(today)

    #this updates the memberID in the database and also the logfile to update when its been returned
    database_update1(database)
    logfile_update(logfile)

