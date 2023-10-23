from datetime import date
import mysql.connector as c
db = c.connect(host = "localhost",user = "root",password = "Jitendrasq@123",database = "librarymanage",auth_plugin = "mysql_native_password")
q1 = "create table if not exists bookl(BookName varchar(255) not null)"
q2 = "create table if not exists userl(name varchar(255) not null,password int not null)"
q3 = "create table if not exists rentl(UName varchar(255),BookName varchar(255),IssueDate date )"
q5 = "create table if not exists submitl(UserName varchar(255),BookName varchar(255),SubmitDate date )"
q6 = "create table if not exists donatel(UserName varchar(255),BookName varchar(255),DonateDate date )"
q4 = "insert into bookl values ('My experiment with truth'),('Nationalism'),('Code complete'),('Motercycle diary'),('Godan'),('Tomb of sand'),('Discovery of india'),('The epic struggle'),('Mathematica')"
cr = db.cursor()
cr.execute(q1)
cr.execute(q2)
cr.execute(q4)
cr.execute(q3)
cr.execute(q5)
cr.execute(q6)
db.commit()
class LibraryM:
    def __init__(self):
        self.rentdict = {}
        self.userdict = {}
        
    def create(self,name,password):
        self.name = name
        self.password = password
        q1 ="insert into userl values(%s,%s)"
        cr = db.cursor()
        cr.execute(q1,(self.name,self.password))
        db.commit()
    def showbooks(self):
        q = "select distinct BookName from bookl"
        cr = db.cursor()
        cr.execute(q)
        x = cr.fetchall()
        n = 1
        for i in x:
            print(f"{n}: {i[0]}")
            n+=1
    def rent(self,bname,date): 
        uname = list(self.userdict.keys())
        rname = uname[0]
        if bname not in self.rentdict.keys():
            self.rentdict.update({bname:rname})
            sql = "insert into rentl values(%s,%s,%s)"
            sql2 = "delete from bookl where BookName = %s"
            cr.execute(sql,(rname,bname,date))
            cr.execute(sql2,(bname,))
            db.commit()
            print(f"Take your book Mr {self.rentdict[bname]} keep reading!!")
        else:
            print(f"Book is already being used by {self.rentdict[bname]}")
    def submit(self,bname,date):
        uname = list(self.userdict.keys())
        sname = uname[0]
        q = "select * from rentl"
        cr = db.cursor()
        cr.execute(q)
        x = cr.fetchall()
        count = 0
        for i in x:
            if i[0] == sname and i[1] == bname:
                count+=1
                break
        if count == 1: 
            print(f"Thank you for returning {bname} book!!")
            sql1 = "insert into bookl values(%s)"
            sql2 = "insert into submitl values(%s,%s,%s)"
            sql3 = "delete from rentl where BookName = %s"
            cr.execute(sql3,(bname,))
            cr.execute(sql2,(sname,bname,date))
            cr.execute(sql1,(bname,))
            db.commit()
        else:
            print("You have not take this book before! Enter right book.")
    def donate(self,bname,date):
        uname = list(self.userdict.keys())
        dname = uname[0]    
        sql1 = "insert into donatel values(%s,%s,%s)"
        cr.execute(sql1,(dname,bname,date))
        sql = "insert into bookl values(%s)"
        cr.execute(sql,(bname,))
        db.commit()
        print(f"Thank you {name} for donating '{bname}' book 🤍")
    def history(self):
        uname = list(self.userdict.keys())
        hname = uname[0]
        q1 = "select BookName,IssueDate from rentl where UName = %s"
        cr = db.cursor()
        cr.execute(q1,(hname,))
        r = cr.fetchall()
        print("**************************")
        print("    YOUR BOOK HISTORY     ")
        print("Rented Books")
        print("Books        Date")
        for i in r:
            print(f"{i[0]}      {i[1]}")
        print()
        q2 = "select BookName,SubmitDate from submitl where UserName = %s"
        sr = db.cursor()
        sr.execute(q2,(hname,))
        s = sr.fetchall()
        print("Submited Books")
        print("Books        Date")
        for i in s:
            print(f"{i[0]}      {i[1]}")
        print()
        q3 = "select BookName,DonateDate from donatel where UserName = %s"
        dr = db.cursor()
        dr.execute(q3,(hname,))
        d = dr.fetchall()
        print("Donated Books")
        print("Books        Date")
        for i in d:
            print(f"{i[0]}      {i[1]}")
        print("**************************")
        
if __name__ == '__main__':
    cl = LibraryM()
    def inside():
        while True:
            print("""
1 : For Available Books 
2 : For Rent a Book
3 : For Submit a Book
4 : For Donate a Book
5 : For Your Book History
6 : For Logout """)
            print()
            inpt = input("Enter your input-- ")
            print()
            if inpt == "1":
                cl.showbooks()
            elif inpt == "2":
                bname = input("Enter Book name--")
                rdate = input("Enter Today date in this format YYYY-MM-DD ")
                cl.rent(bname,rdate)
            elif inpt =="3":
                bname = input("Enter Book name--")
                sdate = input("Enter Today date in this format YYYY-MM-DD ")
                cl.submit(bname,sdate)
            elif inpt == "4":
                bname = input("Enter Book name--")
                ddate = input("Enter Today date in this format YYYY-MM-DD ")
                cl.donate(bname,ddate)
            elif inpt == "5":
                cl.history()
            elif inpt == "6":
                cl.userdict.pop(name)
                print("Logout Successfully !")
                exit()
            else:
                print("Wrong Input, Try again !")
                print()
    while True:
        print("""
        📚 WELCOME IN PUBLIC LIBRARY 📚
1 : FOR LOGIN 
2 : FOR CREATE ACCOUNT
3 : FOR EXIT """)
        print()
        inp = input("Your Input-- ")
        print()
        if inp == "1":
            name = input("Enter your Name--")
            password = int(input("Enter Your password--"))
            q = "select * from userl"
            cr = db.cursor()
            cr.execute(q)
            x = cr.fetchall()
            count = 0
            for i in x:
                if i[0] == name and i[1] == password:
                    count+=1
                    break
            if count == 1:
                cl.userdict.update({name:password})
                print("Login Successfully")
                print()
                inside()
            else:
                print("Wrong Name or Password")
                print()    
        elif inp == "2":
            name = input("Enter Your Name--")
            password = int(input("Enter Your Password--"))
            cpass = int(input("Confirm Password--"))
            q = "select * from userl"
            cr = db.cursor()
            cr.execute(q)
            x = cr.fetchall()
            count = 0
            for i in x:
                if i[1] == password: 
                    count+=1
            if count == 0 and cpass == password:
                cl.userdict.update({name:password})
                cl.create(name,password)
                print("Account Created Successfully!")
                print()
                inside()
                
            else:
                print("Something Wrong in password.Try again")
                print()
        elif inp == "3":
            print("THANK YOU FOR VISITING !")
            exit()
