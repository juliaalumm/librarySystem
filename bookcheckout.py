from datetime import datetime
from datetime import date
from database import *
from tkinter import *
lines = []
liness = []
final = []
database1 = []
logfile = []
database =[]

def book_checkout(book_checkout_tab,memberID,bookID):

    """
    F119883
    16 December 2021
    :param book_checkout_tab:
    :param memberID:
    :param bookID:
    :return:
    this function edits the logfile and database whenever someone wants to check out a book
    """

    #opens the logfile.txt and database.txt
    database_open(database)
    logfile_open(logfile)

    #changes it to a dictionary so its easier to access
    for line in database:
        lines.append({
            "ID":line[0],
            "Genre":line[1],
            "Title":line[2],
            "Author":line[3],
            "Date Purchased":line[4],
            "Member ID":line[5]
        })

    # if the user enter the correct memberID then an error message will appear
    if len(memberID) != 4:
        label = Label(book_checkout_tab,text="Member ID error. Please try again and ensure its a four letter word",
                      font = ("Arial",20), fg = "red").pack()

    for i in lines:
        # seeing which book ID matches with the ID in the textfile and changes the member after they have checked out a book
        if bookID == i['ID'] and i["Member ID"] == "0":
            i["Member ID"]=memberID
            Label(book_checkout_tab, text = "Book Checkout Successful", font = ("Arial",30,"bold"), fg = "#6aa84f").pack()
            for i in lines:
                liness.append(i)
                for n in liness: #to remove the keys in the dictionary and to change it back into a list
                    new_list = list(n.values())
                final.append(new_list)
                for f in final: #to reorder the list since it changed into an unordered dictionary
                    order = [0,1,2,3,4,5]
                    new_final = [f[i] for i in order]
                database1.append(new_final)
            break
        #checks if the bookID matched the ID in the database and if the book is aready checked out since its not zero
        elif bookID == i["ID"] and "0" != i['Member ID']:
            Label(book_checkout_tab, text = "Book has already been checked out", font = ("Arial",20)).pack()
            break
    else:
        Label(book_checkout_tab, text="Book ID Invalid", font=("Arial", 20)).pack()


    #checking if the books have been checked out for more than 60 days
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    today = today[:6] + '20'+today[-2:]
    for i in logfile:
        #checking if the book hasnt been checked out yet and also if the member has checked out this book our not
        if i[2] == "0" and memberID == i[3]:
            date_format = "%d/%m/%Y"
            a = datetime.strptime(i[1], date_format)
            b = datetime.strptime(today, date_format)
            delta = b - a
            dayDiff = delta.days
            #if the book has been checked out for 60 days and if the member ID matches it or not
            if dayDiff >= 60 and memberID == i[3]:
                for l in database1:
                    if i[0] == l[0]:
                        Label(book_checkout_tab, text = "Member has a book checked out for " + str(dayDiff) + " days", font = ("Arial",20,"bold"), fg = "red").pack()
                        Label(book_checkout_tab, text = l[0] + " , " + l[1] + " , " + l[2] + " , " + l[3] + " , " + l[4] + " , " + l[5], font = ("Arial",20,), fg = "red").pack()

    #to add another row to the logfile to show that someone has checked out the book
    for i in database1:
        if bookID == i[0]:
            genre = i[1]
            logfile.append([bookID,today,"0",memberID,genre])

    # this updates the memberID in the database and also the logfile to update when its been returned
    database_update1(database1)
    logfile_update(logfile)


