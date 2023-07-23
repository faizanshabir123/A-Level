StudentAccounts = []
NumberStudents = 0

class PrintAccount:
    def __init__(self,FirstName,LastName,PrintID):
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__PrintID = PrintID
        self.__Credits = 50
    # set methods
    def SetFirstName(self,name):
        self.__FirstName = name
    # get methods
    def GetName(self):
        return(self.__FirstName+" "+self.__LastName)
    def GetPrintID(self):
        return(self.__PrintID)
    def GetCredits(self):
        return(self.__Credits)
        
    def AddCredits(self,MoneyInput):
        ExtraCredit1 = 50
        ExtraCredit2 = 25
        if MoneyInput >= 20:
            self.__Credits = (self.__Credits) + (25*MoneyInput) + ExtraCredit1
        elif (MoneyInput >= 10) and (MoneyInput <=19):
            self.__Credits = self.__Credits + (25*MoneyInput) + ExtraCredit2
        else:
            self.__Credits = self.__Credits + (25*MoneyInput)

def main():
    def CreateID(FirstName,LastName):
        PrintId = (FirstName[0:3]+LastName[0:3]+'1').lower()
        for count in range(len(StudentAccounts)):
            if (StudentAccounts[count].GetPrintID() == PrintId):
                temp = str(int(PrintId[-1]) + 1)
                PrintId = (FirstName[0:3]+LastName[0:3]+temp).lower()
        
        Account = PrintAccount(FirstName,LastName,PrintId)
        StudentAccounts.append(Account)
        NumberStudents = len(StudentAccounts)

    quantity = int(input("How many accounts"))
    for j in range(quantity):
        firstname = input("Enter First Name")
        lastname = input("Enter Last Name")
        CreateID(firstname,lastname)
        MoneyInput = int(input("You get 50 credits for free, if you want to buy more, make payment"))
        StudentAccounts[j].AddCredits(MoneyInput)

    print("Outputting all accounts")
    for k in range(len(StudentAccounts)):
        print("Name is: ",StudentAccounts[k].GetName())
        print("PrintId is: ",StudentAccounts[k].GetPrintID())
        print("Credits are: ",StudentAccounts[k].GetCredits())
main()
        
        
        
        
        
            
        
            

        
            
             
            
        
                
        
    
    
            
            
            
        
        
