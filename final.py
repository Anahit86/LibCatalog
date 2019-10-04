from configparser import ConfigParser
import time
import configparser


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

def create_new_file(section,option,value):
    config=configparser.ConfigParser()
    config.read("temp.txt")
    config.set(section,option,value)
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
    print("This book is now anavailable, please type YES if you want to reserve, or NO if you don't")
    wish = input()
    if wish =="YES":
        config=configparser.ConfigParser()
        config.read("temp.txt")
        a = config["reserve"]["name"]
        create_new_file("reserve","name",a+ ","+user1.name)

def available_book(book):
    for ip in ISBN1:
        if book==fil1[ip]["title"]:
            print("The available count of this book is %s" %(fil1[ip]['available_copies']))
def check_out_book(book):
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
                checkout_time= time.asctime(time.localtime(time.time()))
#                create_new_file("reserve"","check_out_time",checkout_time)
                break
            elif s==0:
                reserve_book(user1.name,book)
def return_book(book):
    for ip in ISBN1:
        if book==fil1[ip]["title"]:
            c = fil1.getint(ip,'available_copies')
            c +=1
            fil1[ip]['available_copies'] = str(c)
            fil1.set(ip,"available_copies", str(c))
            with open ("books.txt", "r+") as f:
                fil1.write(f)
                f.close()
            return_time= time.asctime(time.localtime(time.time()))
#            create_new_file("reserve","return_time",return_time)
            print("The book is returned succesfully")
def reserve_user_list(file):
    config = configparser.ConfigParser()
    config.read(file)
    print(config ["reserve"]["name"])
    return config ["reserve"]["name"]
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
"""
User checkout book
- Allow user to checkout a book. The value of available copies of the book should
be reduced. Save the time of check-out to further check if the book is overdue
and compute the fine.
"""
## If no available copies
"""
User reserve book (subscribe)
- Allow user to put a book in reserve if it is not available
"""
#user1 = user(username)
#user1.check_user()
#book1 = book(ISBN1, tit,ac)
#book1.check_book()
#check_out_book(book1.book_name)
"""
User return book
- Allow user to return a book. The value of available copies of the book should be
increased.
"""
#book1 = book(ISBN1, tit,ac)
#book1.check_book()
#return_book(book1.book_name)
"""
Get subscribers of the book
- Get the list of users that have put the book on reserve
"""
#user1 = user(username)
#user1.check_user()
#book1 = book(ISBN1, tit,ac)
#book1.check_book()
#reserve_user_list("temp.txt")
"""
Check book is available
- Check if available copy of book is present
"""
#book1 = book(ISBN1, tit,ac)
#book1.check_book()
#available_book(book1.book_name)
""""
Add user
- Add user info to the LibraryCatalog, so that it’s saved in Users info file in same
format as others. Get info from standard input.
"""
#add_user()
"""
Add book (get info from standard input)
- Add book info to the LibraryCatalog, so that it’s saved in Books info file in same
format as others. Get info from standard input.
"""
#add_book()
"""
Remove user
- Remove user info to the LibraryCatalog, so that it’s removed form Users info
file.
"""
#remove_user()
"""
Remove book
- Remove book info to the LibraryCatalog, so that it’s removed form Users info
file.
"""
#remove_book()
