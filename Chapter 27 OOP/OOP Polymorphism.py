# ch 27 OOP
# Inheritance
# Polymorphism

import datetime
class LibraryItem:
    def __init__(self, t, a, i):   # # initialiser method
        self.__Title = t
        self.__Author__Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()

    def GetTitle(self):
        return(self.__Title)
# other Get methods go here
    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks-3)

    def Returning(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print("Title is: ",self.__Title,"Author/Artist is:",self.__Author__Artist)
        print("Item ID is: ",self.__ItemID,"OnLoan Is: ",self.__OnLoan,"DueDate is:",self.__DueDate)

class Book(LibraryItem):  # initialiser method
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = 0

    def GetIsRequested(self):
        return(self.__IsRequested)
    def SetIsRequested(self):
        self.__IsRequested = True

    def PrintDetails(self): # Polymorphism
        print("Book Details")
        LibraryItem.PrintDetails(self) # self argument imp # This line calls the base class method with the same name.
        print("IsRequested is: ",self.__IsRequested)

class CD(LibraryItem):    # initialiser method
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""

    def GetGenre(self):
        return(self.__Genre)

    def SetGenre(self, g):
        self.__Genre = g

    def PrintDetails(self): # Polymorphism
        print("CD Details")
        LibraryItem.PrintDetails(self) # self argument imp # This line calls the base class method with the same name.
        print("Genre is: ",self.__Genre)

def main():
    t = input("Enter book title")
    a = input("Enter book Author")
    i = input("Enter ItemID")
    book = Book(t,a,i)
    print("Outputting Details")
    book.PrintDetails()

    t = input("Enter cd title")
    a = input("Enter Artist")
    i = input("Enter ItemID")
    cd = CD(t,a,i)
    g = input("Enter Genre")
    cd.SetGenre(g)
    print("Outputting Details")
    cd.PrintDetails()
    
main()

    
    





