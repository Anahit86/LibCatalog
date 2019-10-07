from configparser import ConfigParser
import time
import configparser
import datetime
import sys



parser= ConfigParser()
config_file_list= ["books.txt","users.txt"]
file1= config_file_list[0]
file2 = config_file_list[1]

fil1 = configparser.ConfigParser()
fil2 = configparser.ConfigParser()
fil1.read(file1)
fil2.read(file2)

ISBN1 = fil1.sections()
tit = [fil1[s]['title'] for s in ISBN1]
ac = [fil1[s]['available_copies'] for s in ISBN1]

userid=fil2.sections()
username=[fil2[s]["name"] for s in userid]

def update_temp_file(book, name,*argv):
    config=configparser.ConfigParser()
    config.read("temp.txt")
    sec = book + "_" + name
    if config.has_section(sec):
        config.set(sec,argv[0],argv[1])
    else:
        config.add_section(sec)
        config.set(sec,argv[0],argv[1])
    with open("temp.txt", 'r+') as f:
        config.write(f)
        f.close()


class user:
    def __init__(self,name):
        self.name=name
        self.nameid=userid
    def check_user(self):
        while True:
            try:
                self.name= input("input your username")
                if self.name not in username:
                    raise Exception
            except Exception:
                print("This username is not in list, please select from the list", "\n", username)
            else:
                if self.name in username:
                    break
                    return self.name
class book:
    def __init__(self,ISBN,book_name,available_count):
        self.ISBN=ISBN
        self.book_name=book_name
        self.available_count=available_count
    def check_book(self):
        while True:
            try:
                self.book_name = input("Enter prefered book")
                if self.book_name not in tit:
                    raise Exception
            except Exception:
                print("The book is not in the library, please take one from the following list", "\n", tit)
            else:
                if self.book_name in tit:
                    break
                    return self.book_name

def reserve_book(book,name):
    print("This book is now unavailable, please type YES if you want to reserve, or NO if you don't")
    wish = input()
    if wish =="YES":
        update_temp_file(book,name,"reserve_user",name)

def available_book(book):
    for ip in ISBN1:
        if book==fil1[ip]["title"]:
            print("The available count of this book is %s" %(fil1[ip]['available_copies']))
def check_out_book(book,name):
    for ip in ISBN1:
        if book==fil1[ip]["title"]:
            s = fil1.getint(ip,'available_copies')
            if s > 0:
                c = fil1.getint(ip,'available_copies')
                c -=1
                fil1[ip]['available_copies'] = str(c)
                fil1.set(ip,"available_copies", str(c))
                with open ("books.txt", "r+") as f:
                    fil1.write(f)
                    f.close()
                checkout_time=datetime.date.today()
                for i in S:
                    if book +"_"+name==i and config.has_option(i,"reserve_user"):
                        config.remove_option(i,"reserve_user")
                        with open('temp.txt', 'w') as f:
                            config.write(f)
                            f.close()
                print(checkout_time)
                update_temp_file(book,name,"check_out_time",str(checkout_time))
                update_temp_file(book,name,"check_out_by_user",name)
                break
            elif s==0:
                reserve_book(book,name)
def return_book(book,name):
    for ip in ISBN1:
        if book==fil1[ip]["title"]:
            c = fil1.getint(ip,'available_copies')
            c +=1
            fil1[ip]['available_copies'] = str(c)
            fil1.set(ip,"available_copies", str(c))
            with open ("books.txt", "r+") as f:
                fil1.write(f)
                f.close()
            return_time=datetime.date.today()
            update_temp_file(book,name,"return_time",str(return_time))
            print("The book is returned succesfully")
def reserve_user_list(file,book):
    config = configparser.ConfigParser()
    config.read(file)
    S= config.sections()
    L= [config[i]["reserve_user"] for i in S if config.has_option(i,"reserve_user")]
    print(L)
def add_user():
    nameid= input("enter the username id:")
    name = input("enter user name for adding the list:")
    if len(nameid) == 4:
        parser.add_section(nameid)
        parser.set(nameid,"name",name)
        with open('users.txt', 'a') as f:
            parser.write(f)
            f.close()
def add_book():
    ISBN= input("enter the ISBN:")
    title= input("book title:")
    pages=input("the book pages:")
    copies=input("the count of the book:")
    available_copies= input("the availabe count of the book:")
    if len(ISBN) == 10:
        parser.add_section(ISBN)
        parser.set(ISBN,"title",title)
        parser.set(ISBN,"pages",pages)
        parser.set(ISBN,"copies",copies)
        parser.set(ISBN,"available_copies",available_copies)
        with open('books.txt', 'a') as f:
            parser.write(f)
            f.close()
    else:
        print("the ISBN is not correct. Insert ID with 10 digits")
def remove_user():
    nameid= input("enter the username id:")
    name = input("enter user name for removeing the list:")
    if len(nameid) == 4:
        parser.read("users.txt")
        parser.remove_option(nameid,"name")
        parser.remove_section(nameid)

        with open('users.txt', 'w') as f:
           parser.write(f)
           f.close()
def remove_book():
    ISBN= input("enter the ISBN:")
    title= input("book title:")
    pages=input("the book pages:")
    copies=input("the count of the book:")
    available_copies= input("the availabe count of the book:")
    if len(ISBN) == 10:
        parser.read("books.txt")
        parser.remove_option(ISBN,"title")
        parser.remove_option(ISBN,"pages")
        parser.remove_option(ISBN,"copies")
        parser.remove_option(ISBN,"available_copies")
        parser.remove_section(ISBN)
        with open('books.txt', 'w') as f:
            parser.write(f)
            f.close()
def overdue_books(file,name):
    from datetime import datetime
    config = configparser.ConfigParser()
    config.read(file)
    S = config.sections()
    OB =list()
    OD = 0
    for i in S:
        if name in i and config.has_option(i,"check_out_time") and config.has_option(i,"return_time"):
            t1 =config[i]["check_out_time"]
            t2 =config[i]["return_time"]
            L= datetime.strptime(t2,'%Y-%m-%d')-datetime.strptime(t1,'%Y-%m-%d')
            if L.days> 90:
                for book in tit:
                    if book in i:
                        print("the overdue book list checked out by %s" %(name))
                        OB.append(book)
                        OD =((OD + (L.days-90)))
                        print(OB)
            else:
                print("You have no overdue books")
    print("The total fine is %s$" %((OD/7)*5))
def overdue_book_fine(file,name,book):
    from datetime import datetime
    config = configparser.ConfigParser()
    config.read(file)
    S = config.sections()
    sec=book + "_" + name
    OB =list()
    if sec in S:
        if config.has_option(sec,"check_out_time") and config.has_option(sec,"return_time"):
            t1 =config[sec]["check_out_time"]
            t2=config[sec]["return_time"]
            L= datetime.strptime(t2,'%Y-%m-%d')-datetime.strptime(t1,'%Y-%m-%d')
            if L.days> 90:
                OD=L.days-90
                fine =(OD/7)*5
                print("this book is overdue %s days.the fine is %s$  for user %s" %(OD,fine,name))
                return fine
            else:
                print("This book is not overdue")
        elif config.has_option(i,"check_out_time") or config.has_option(i,"return_time"):
            print("you have not check_out/return the book")
def checkout_user_list(file,book):
    config = configparser.ConfigParser()
    config.read(file)
    S= config.sections()
    L= [config[i]["check_out_by_user"] for i in S if book in i and config.has_option(i,"check_out_by_user") ]
    print(L)

def main():
    donw=False
    while donw==False:
        print("""\
            Please enter the the action number which you want to do:
            ===========================
            1. Checkout a book
            2. Return Book
            3. Reserve Book
            4. Get reserve user list
            5. Overdue books
            6. Get user overdue book fine
            7. Abailable of book
            8. User list who checked out the book
            9. Add user
            10. Add Book
            11. Remove user
            12. Remove book
            13. Exit

            """)
        case = int(input())
        if case ==1:
            user1 = user(username)
            user1.check_user()
            book1 = book(ISBN1, tit,ac)
            book1.check_book()
            check_out_book(book1.book_name,user1.name)
        if case ==2:
            user1 = user(username)
            user1.check_user()
            book1 = book(ISBN1, tit,ac)
            book1.check_book()
            return_book(book1.book_name,user1.name)
        if case ==3:
            user1 = user(username)
            user1.check_user()
            book1 = book(ISBN1, tit,ac)
            book1.check_book()
            check_out_book(book1.book_name)
        if case ==4:
            user1 = user(username)
            user1.check_user()
            book1 = book(ISBN1, tit,ac)
            book1.check_book()
            reserve_user_list("temp.txt",book1.book_name)
        if case ==5:
            user1 = user(username)
            user1.check_user()
            overdue_books("temp.txt",user1.name)
        if case ==6:
            user1 = user(username)
            user1.check_user()
            book1 = book(ISBN1, tit,ac)
            book1.check_book()
            overdue_book_fine("temp.txt",user1.name,book1.book_name)
        if case ==7:
            book1 = book(ISBN1, tit,ac)
            book1.check_book()
            available_book(book1.book_name)
        if case ==8:
            book1 = book(ISBN1, tit,ac)
            book1.check_book()
            checkout_user_list("temp.txt",book1.book_name)
        if case ==9:
            add_user()
        if case ==10:
            add_book()
        if case ==11:
            remove_user()
        if case ==12:
            remove_book()
        if case==13:
            sys.exit()


main()
