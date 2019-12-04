import configparser
import datetime
import sys


class mydict:
    def __init__(self, file):
        self.file = file

    def makedict(self):
        book1 = configparser.ConfigParser()
        book1.optionxform = str
        book1.read(self.file)
        fin = {}
        for i in book1.sections():
            KEY = book1.options(i)
            a = {}
            for op in KEY:
                a[op]= book1.get(i,op)
            fin[i]= a
        return fin


def writefile(file,dict):
    config=configparser.ConfigParser()
    config.optionxform = str #All option names are passed through the optionxform() method. Its default implementation
                            # converts option names to lower case. disable this behaviour
    config.read(file)
    print(config.sections())
    for i, v in dict.items():
        for val in range(len(dict[i].keys())):
            l = list(dict[i].values())
            k = list(dict[i].keys())
            config.set(i,str(k[val]),str(l[val]))
            with open(file, 'w+') as f:
                config.write(f)

def add_new_section_in_file(file,dict):
    config=configparser.ConfigParser()
    config.optionxform = str #All option names are passed through the optionxform() method. Its default implementation
                             # converts option names to lower case. disable this behaviour
    config.read(file)
    for i, v in dict.items():
        for val in range(len(dict[i].keys())):
            l = list(dict[i].values())
            k = list(dict[i].keys())
            config.add_section(i)
            config.set(i,str(k[val]),str(l[val]))
            with open(file, 'w+') as f:
                config.write(f)

def remove_from_file(file,dict):  #dict is a remove_book/remove_user function result
    config=configparser.ConfigParser()
    config.optionxform = str #All option names are passed through the optionxform() method.
                             # Its default implementation converts option names to lower case. disable this behaviour
    config.read(file)
    config.remove_section(dict)
    with open(file, 'w+') as f:
        config.write(f)

class book:
    def __init__(self,dict):
        self.id=list(dict.keys())
        self.title = [dict[s]['title'] for s in self.id]
        self.page= [dict[s]['pages'] for s in self.id]
        self.copy = [dict[s]['copies'] for s in self.id]
        self.ac = [dict[s]['available_copies'] for s in self.id]
        self.booklist = {dict[s]['title']:s for s in self.id}
        self.checkoutList = {dict[s]['title']:dict[s]['checkout'] for s in self.id if 'checkout' in dict[s].keys()}
        self.reserveList = {dict[s]['title']:dict[s]['reserve'] for s in self.id if 'reserve' in dict[s].keys()}

    def availableBooks(self,dic):
        availableBooks = {dic[s]['title']:dic[s]['available_copies'] for s in self.id}
        return availableBooks

    def returnbookid(self,askforbook):
        id = self.booklist[askforbook]
        return [askforbook, id]

    def totaltime(self,dic,name):
        checkoutTime= {dic[s]['title']:(dic[s]['checkouttime_for_%s' % name] +','+dic[s]['returntime_for_%s' % name])
                       for s in self.id
                       if (('checkouttime_for_%s' % name) in dic[s].keys()) and
                          (('returntime_for_%s' % name) in dic[s].keys()) }
        print(checkoutTime)
        return checkoutTime


class user:
    def __init__(self,dict):
        self.id= list(dict.keys())
        self.namelist= [dict[s]['name'] for s in self.id]
        while True:
            try:
                self.name= input("input your username")
                if self.name not in self.namelist:
                    raise Exception
            except Exception:
                print("This username is not in list, please select from the list", "\n",self.namelist)
            else:
                if self.name in self.namelist:
                    break

    def askforBook(self,title):
        while True:
            try:
                book= input("Please enter the book name you want to check out:")
                if book not in title:
                    raise Exception
            except Exception:
                print("This book is not in list, please select from the list", "\n", title)
            else:
                if book in title:
                    break
        return book

    def returnBook(self,title):
        while True:
            try:
                book= input("Please enter the book name you want to return:")
                if book not in title:
                    raise Exception
            except Exception:
                print("This book is not in list, please select from the list", "\n", title)
            else:
                if book in title:
                    break
        return book

    def checkBookOverdueorNot(self,title):
        while True:
            try:
                book= input("Please enter the book name you want to check:")
                if book not in title:
                    raise Exception
            except Exception:
                print("This book is not in list, please select from the list", "\n", title)
            else:
                if book in title:
                    break

        return book

    def reserveBook(self,title):
        while True:
            try:
                book= input("Please enter the book name you want to check:")
                if book not in title:
                    raise Exception
            except Exception:
                print("This book is not in list, please select from the list", "\n", title)
            else:
                if book in title:
                    break

        return book

    def checkBookAvailableorNot(self,title):
        while True:
            try:
                book= input("Please enter the book name you want to check:")
                if book not in title:
                    raise Exception
            except Exception:
                print("This book is not in list, please select from the list", "\n", title)
            else:
                if book in title:
                    break

        return book

    def addbook(self):
        addbook={}
        id = input("input the isbc")
        title = input("input book title")
        pages = input("input book pages")
        copies = input("input book copies")
        ac = input("input available copies of the book")
        addbook[id] = {}
        addbook[id]["title"]= title
        addbook[id]["pages"]= pages
        addbook[id]["copies"]= copies
        addbook[id]["available_copies"]= ac
        return addbook

    def adduser(self):
        adduser={}
        id = input("input the id")
        name = input("input full name")
        adduser[id] = {}
        adduser[id]["name"]= name
        return adduser

    def remove_book(self):
        id = input("input the isbc")
        return id
    def remove_user(self):
        id = input("input user id")
        return id

class LibraryCatalog:
    def __init__(self,dic):
        self.dic= dic
    def CheckoutBook(self,availableBooks,name,id):
        if id[0] in availableBooks:
            if  'checkout' in self.dic[id[1]].keys() and name in self.dic[id[1]]['checkout']:
                print("You already borrow this book")
            else:
                self.dic[id[1]]['available_copies']= int(availableBooks[id[0]]) -1
                self.dic[id[1]]['checkouttime_for_%s' % name] =datetime.date.today()
                if 'checkout' in self.dic[id[1]].keys():
                    self.dic[id[1]]['checkout']=self.dic[id[1]]['checkout']+','+name
                else:
                    self.dic[id[1]]['checkout']=name
                print("The book you ask is available and checked out by you")
                return self.dic
        else:
            print("The book is  not available.You can select one from this list %s" %availableBooks)
    def CheckoutUserList(self,askforbook,checkoutList):
        if askforbook in checkoutList:
            print("the book ia/are borrowed from the following users")
            print(checkoutList[askforbook])
        else:
            print("No one checked out this book")
    def ReserveUserList(self,reservebook,reserveList):
        if reservebook in reserveList:
            print("the book ia/are reserved from the following users")
            print(reserveList[askforbook])
        else:
            print("No one reserve this book")
    def ReturnBook(self,name,availableBooks,id):
        self.dic[id[1]]['available_copies']= int(availableBooks[id[0]]) +1
        checkout_list= self.dic[id[1]]['checkout']
        print(checkout_list)
        print(id[0],id[1])
        self.dic[id[1]]['returntime_for_%s' % name] =datetime.date.today()
        return self.dic
    def ReserveBook(self,name,id):
        if 'reserve' in self.dic[id[1]].keys():
            self.dic[id[1]]['reserve']=self.dic[id[1]]['reserve']+','+name
        else:
            self.dic[id[1]]['reserve']=name
    def AvailableCopy(self,askforbook,availablebook,name):
        if askforbook  in availablebook and availablebook[askforbook] != 0:
            print("%s available count: %s" %(askforbook,availablebook[askforbook]))
        else:
            print("the book is not available, if you want to reserve type YES")
            case = input()
            if case =='YES':
                print("The book is reserved")
                self.ReserveBook(name)
    def OverdueBookList(self,totaltime):
        OB = list()
        overB= {}
        from datetime import datetime
        for bookname in totaltime.keys():
            tick = totaltime[bookname]
            ticklist= tick.split(',')
            time = datetime.strptime(ticklist[1],'%Y-%m-%d')- datetime.strptime(ticklist[0],'%Y-%m-%d')
            if time.days >90:
                OB.append(bookname)
                overB[bookname]=time.days
        if len(OB) >0:
            print("The overdue book list for you %s" %OB)
        else:
            print("you have no overdue books")
        return overB
    def BookFine(self,checkoverduebook,totaltime):
        if checkoverduebook in self.OverdueBookList(totaltime).keys():
            OD= self.OverdueBookList(totaltime)[checkoverduebook]
            fine = ((OD-90)/7)*5
            print("The book fine is %s$" %fine)
    def TotalFine(self,totaltime):
        totaltimefine=0
        for bk in totaltime.keys():
            totaltimefine=totaltimefine+(self.OverdueBookList(totaltime)[bk]-90)
        print((totaltimefine/7)*5)
    def AddBook(self,addbook,dic):
        id= list(addbook.keys())
        dic[id[0]]= {
                     'title': addbook[id[0]]["title"],
                     'pages': addbook[id[0]]["pages"],
                     'copies': addbook[id[0]]["copies"],
                     'available_copies':addbook[id[0]]["available_copies"]
        }
        return dic
    def AddUser(self,adduser,dic):
        id= list(adduser.keys())
        dic[id[0]]= {'name': adduser[id[0]]["name"]}
        return dic
    def RemoveBook(self,remove_book):
        remove_from_file('books.txt', remove_book)
    def RemoveUser(self,remove_user):
        remove_from_file('users.txt', remove_user)
#####Creating atributes and objects########
#creating object for class mydict for books.txt
dic= mydict("books.txt")
#creating object for class mydict for users.txt
dict= mydict("users.txt")
#creating dictionary for books
lib = dic.makedict()
#creating dictionary for user
person = dict.makedict()
#user class atribute
user1 = user(dict.makedict())
#book class atribute
book1 = book(dic.makedict())
#library class atribute
library= LibraryCatalog(lib)


def main():
    donw=False
    while donw==False:
        print("""\
            Please enter the the action number which you want to do:
            ===========================
            1. Checkout Book
            2. Return Book
            3. Get reserve user list
            4. Get user list who checked out the book
            5. Abailable of book
            6. Overdue books
            7. Get user overdue book fine
            8. Total fine for user
            9. Add Book
            10. Add User
            11. Remove user
            12. Remove book
            13. Exit

            """)
        case = int(input())
        if case ==1:
            library.CheckoutBook(book1.availableBooks(lib),user1.name,book1.returnbookid(user1.askforBook(book1.title)))
            writefile('books.txt',lib)
        if case ==2:
            library.ReturnBook(user1.name,book1.availableBooks(lib),book1.returnbookid(user1.returnBook(book1.title)))
            writefile('books.txt',lib)
        if case ==3:
            library.ReserveUserList(user1.reserveBook(book1.title),book1.reserveList)
        if case ==4:
            library.CheckoutUserList(user1.askforBook(book1.title),book1.checkoutList)
        if case ==5:
            library.AvailableCopy(user1.checkBookAvailableorNot(book1.title),book1.availableBooks(lib),user1.name)
        if case ==6:
            library.OverdueBookList(book1.totaltime(lib,user1.name))
        if case ==7:
            library.BookFine(user1.checkBookOverdueorNot(book1.title),book1.totaltime(lib,user1.name))
        if case ==8:
            library.TotalFine(book1.totaltime(lib,user1.name))
        if case ==9:
            library.AddBook(user1.addbook(), lib)
            add_new_section_in_file('books.txt',lib)
        if case ==10:
            library.AddUser(user1.adduser(), person)
            add_new_section_in_file('users.txt',person)
        if case ==11:
            library.RemoveBook(user1.remove_book())
        if case ==12:
            library.RemoveUser(user1.remove_user())
        if case==13:
            sys.exit()
main()
