
def database_open(database):
    with open("database.txt","r") as f:
        for row in f:
            row = row.strip().split(",")
            database.append(row)

def logfile_open(logfile):
    with open("logfile.txt","r") as l:
        for row in l:
            row = row.strip().split(",")
            logfile.append(row)

def database_update():
    with open ("tester.txt","w") as f:
        for i in database:
            f.write(i)
            f.write("\n")

def database_update1(database):
    with open("database.txt","w") as w:
        for i in database:
            edited = ",".join(i)
            w.writelines(edited)
            w.write("\n")

def logfile_update(logfile):
    with open ("logfile.txt","w") as w:
        for i in logfile:
            edited = ",".join(i)
            w.writelines(edited)
            w.write("\n")
