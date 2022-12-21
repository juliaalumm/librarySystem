from database import *
from tkinter import *
from datetime import datetime
from datetime import date
lines =[]
liness = []
final = []
database1 = []
database=[]
overdue = []
logfile = []
results = []
overdued = []

def book_search(book_search_tab,search):

    """
    F119883
    16 December 2021
    :param book_search_tab:
    :param search:
    :return:
    this function searches for the books by its title
    """

    # opens the logfile.txt and database.txt
    database_open(database)
    logfile_open(logfile)

    # changes it to a dictionary so its easier to access
    for line in database:
        lines.append({
            "ID":line[0],
            "Genre":line[1],
            "Title":line[2],
            "Author":line[3],
            "Date Purchased":line[4],
            "Member ID":line[5]
        })

    #this is the title to show which order it is in
    Label(book_search_tab, text="ID | GENRE | TITLE | AUTHOR | DATE PURCHASED | MEMBER ID",
          font=("Arial", 20, "bold")).pack()

    #where they take the value and search for the books
    for i in lines:
        if search in i["Title"].strip().lower():
            results.append(i)
            result = Label(book_search_tab,text = i["ID"] + " , " + i["Genre"] + " , " + i["Title"] + " , " + i["Author"] + " , " + i["Date Purchased"] + " , " + i["Member ID"], font = ("Arial",17)).pack()

    # checking if the books have been checked out for more than 60 days
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    today = today[:6] + '20'+today[-2:]
    for i in logfile:
        if i[2] == "0":
            date_format = "%d/%m/%Y"
            a = datetime.strptime(i[1], date_format)
            b = datetime.strptime(today, date_format)
            delta = b - a
            dayDiff = delta.days
            if dayDiff >= 60:
                #adding it to a new list so i can compare it with the ones shown
                overdue.append(i)


    #comparing it with the ones shown so it only shows the one that the user searched for
    for i in results:
        for l in overdue:
            if i["ID"] == l[0]:
                overdued.append(i["ID"])

    if overdued != []:
        Label(book_search_tab, text="Book ID's that have been checked out for more than 60 days:",font=("Arial", 20, "bold"), fg="red").pack()
        Label(book_search_tab, text=overdued, font=("Arial", 20), fg="red").pack()
