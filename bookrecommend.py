from collections import Counter
from tkinter import *
from database import *
database = []
logfile = []
favBook = []
userGenre = []
overall = []
overallT = []

def bookrecommend(book_recommend_tab,memberID):
    """
    F119883
    16 December 2021
    :param book_recommend_tab:
    :param memberID:
    :return:
    this functions collects the most viewed books and the users most viewed genre and helps recommend them books and also show a graph on how many total times the book was checked out
    """

    #if the user enter the correct memberID then an error message will appear
    if len(memberID) != 4:
        label = Label(book_recommend_tab,text="Member ID error. Please try again and ensure its a four letter word",
                      font = ("Arial",20), fg = "red").pack()

    #opens the logfile.txt and database.txt
    database_open(database)
    logfile_open(logfile)

    #finding the users favorite genere
    for i in logfile:
        if i[3] == memberID:
            favBook.append(i[0])

    for i in favBook:
        for l in database:
            if i == l[0]:
                userGenre.append(l[1])

    #lets the user know which genre is their favorite and also helps find the most common genre occurence in the list userGenre
    c = Counter(userGenre)
    favGenre = c.most_common(1)
    favGenre = [i[0] for i in favGenre]
    favGenre = "".join(favGenre)
    Label(book_recommend_tab,text = "Top Genre is "+ str(favGenre), font = ("Arial",20,"bold")).pack(pady= (0,30))

    #finding overall most popular books in the logfile
    for i in logfile:
        if favGenre == i[4]:
            overall.append(i[0])

    for i in overall:
        for l in database:
            if i == l[0]:
                overallT.append(l[2])

    #find the top 5 most popular books in members favorite genre and lets the user know
    c = Counter(overallT)
    mostPopular = c.most_common(5)
    mostPopular1 = [i[0] for i in mostPopular] #arranged in order
    Label(book_recommend_tab, text = "Top Recommended Books:",font=("Arial",20,"bold")).pack(pady = (0,10))
    for i in mostPopular:
        Label(book_recommend_tab, text= i[0], font=("Arial",20)).pack()

    import math
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    import numpy as np

    #here the graph is created to show how many times the top 5 books have been borrowed through the whole logfile
    mostPopularD = dict(mostPopular)
    title = list(mostPopularD.keys())
    popularity = list(mostPopularD.values())
    plt.bar(range(len(mostPopularD)),popularity,tick_label=title)
    plt.title("Your Top Recommended Books")
    plt.xlabel("Movie Title")
    plt.ylabel("Number of times borrowed")

    #to ensure that it only shows if the user input a valid memberID
    if len(memberID) == 4:
        plt.show()