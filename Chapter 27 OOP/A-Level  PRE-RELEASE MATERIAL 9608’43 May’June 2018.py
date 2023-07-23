# A-Level PRE-RELEASE MATERIAL 9608/43 May/June 2018
# Task 2

List1 = []
List2 = []

class toy:
    def  __init__(self,Name,ID):
        self.__Name = Name
        self.__ID = ID
        self.__Price = 0
        self.__MinimumAge = 0
    # get methods
    def GetName(self):
        return(self.__Name)
    def GetID(self):
        return(self.__ID)
    def GetPrice(self):
        return(self.__Price)
    def GetMinimumAge(self):
        return(self.__MinimumAge)
    # set methods
    def SetPrice(self,p):
        self.__Price = p
    def SetMinimumAge(self,a):
        while (a <= 0) or (a >= 18):
            a = int(input("Please enter age between 0 and 18"))
        self.__MinimumAge = a
        
class ComputerGame(toy):
    def __init__(self,Name,ID):
        toy.__init__(self,Name,ID)
        self.__Category = ""
        self.__Console = ""
    # get methods
    def GetCategory(self):
        return(self.__Category)
    def GetConsole(self):
        return(self.__Console)
    # set methods
    def SetCategory(self,cat):
        self.__Category = cat
    def SetConsole(self,con):
        self.__Console = con

class Vehicle(toy):
    def __init__(self,Name,ID,Type,Height,Length,Weight):
        toy.__init__(self,Name,ID)
        self.__Type = Type
        self.__Height = Height
        self.__Length = Length
        self.__Weight = Weight
    # get methods
    def GetType(self):
        return(self.__Type)
    def GetHeight(self):
        return(self.__Height)
    def GetLength(self):
        return(self.__Length)
    def GetWeight(self):
        return(self.__Weight)

def details():
    InList1 = False
    InList2 = False
    Id = input("Enter ID")

    for count in range(len(List1)):
        if List1[count].GetID() == Id:
            InList1 = True
            break
    if InList1 == False:
        for count in range(len(List2)):
            if List2[count].GetID() == Id:
                InList2 = True
                break

    if InList1 == True:
        print("Name is: ",List1[count].GetName())
        print("Price is: ",List1[count].GetPrice())
        print("Minimum Age is: ",List1[count].GetMinimumAge())
        print("Category is: ",List1[count].GetCategory())
        print("Console is: ",List1[count].GetConsole())
    elif InList2 == True :
        print("Name is: ",List2[count].GetName())
        print("Price is: ",List2[count].GetPrice())
        print("Minimum Age is: ",List2[count].GetMinimumAge())
        print("Type is:",List2[count].GetType())
        print("Height is: ",List2[count].GetHeight())
        print("length is: ",List2[count].GetLength())
        print("Weight is: ",List2[count].GetWeight())
    else:
        print("Not found")
        
def main():
    quantity = int(input("For how many toys do you want to enter data "))
    for i in range(quantity):
        Type = input("Is it a ComputerGame(CG) or a Vehicle(V) ")
        if Type == "CG":
            name = input("Enter name")
            Id = input("Enter ID")
            temp = ComputerGame(name,Id)

            price = input("Enter price")
            temp.SetPrice(price)

            MinAge = int(input("Enter MinimumAge"))
            temp.SetMinimumAge(MinAge)

            category = input("Enter category")
            temp.SetCategory(category)

            console = input("Enter Console")
            temp.SetConsole(console)
            List1.append(temp)
        else:
            name = input("Enter name")
            Id = input("Enter ID")
            price = input("Enter price")
            MinAge = int(input("Enter MinimumAge"))
            typ = input("Enter Type of Vehicle")
            height = input("Enter height of Vehicle")
            length = input("Enter length of Vehicle")
            weight = input("Enter weight of Vehicle")
            temp = Vehicle(name,Id,typ,height,length,weight)
            temp.SetPrice(price)
            temp.SetMinimumAge(MinAge)
            List2.append(temp)

    choice = input("Do you to find a toy y or n")
    while choice == "y":
        details()
        choice = input("Do you want to find more toys y or n")

main()
        

            

            

            
            
            
            
        
    

        
        
 

    
