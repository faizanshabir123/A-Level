class Car:
    def __init__(self,i,e):
        self.__vid = i
        self.__engine = e
        self.__price = 0.0
        self.__reg = ""
        self.__dop = ""

    #setter methods
    def setprice(self,p):
        self.__price = p
    def setreg(self,r):
        self.__reg = r
    def setdop(self,d):
        self.__dop = d
    
    #getter methods
    def getprice(self):
        return(self.__price)
    def getreg(self):
        return(self.__reg)
    def getdop(self):
        return(self.__dop)
    def getengine(self):
        return(self.__engine)
    def getid(self):
        return(self.__vid)
def main():
    TempID = ""
    TempEngine = 0
    duty=0.0
    TempID = input("Enter vehicle ID")
    TempEngine = int(input("enter engine size"))
    MyCar = Car(TempID,TempEngine)
    TempPrice = 0.0
    TempReg = ""
    Tempdop = ""
    TempPrice=float(input("Enter the purchase price"))
    Tempdop = input("enter the date of purchase")
    TempReg = input("enter the name of registered owner")
    MyCar.setprice(TempPrice)
    MyCar.setdop(Tempdop)
    MyCar.setreg(TempReg)

    print("This is the Vehicle ID ",MyCar.getid())
    print("this is the registered owner ",MyCar.getreg())
    print("This is the engine size ",MyCar.getengine())
    duty = .50*(MyCar.getengine())
    print("The duty for this car is ",duty)
    print("This is the date of Purchase ",MyCar.getdop())
    print("This Vehicle was purchased for ",MyCar.getprice())
    

main()


    
    
    
