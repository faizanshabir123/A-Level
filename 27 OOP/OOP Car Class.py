# Ch 27 opp
# car class
class Car:
    def __init__(self, n, e):      # constructor
        self.__VehiclelD = n
        self.__Registration = ""
        self.__Date0fRegistration = None
        self.__EngineSize = e
        self.__PurchasePrice = 0.00

    def SetPurchasePrice(self, p):
        self.__PurchasePrice = p
    def SetRegistration(self, r):
        self.__Registration = r
    def SetDateOfRegistration(self, d):
        self.__Date0fRegistration = d

    def GetVehicleID(self):
        return(self.__VehiclelD)
    def GetRegistration(self):
        return(self.__Registration)
    def GetDate0fRegistration(self):
        return(self.__Date0fRegistration)
    def GetEngineSize(self):
        return(self.__EngineSize)
    def GetPurchasePrice(self):
        return(self.__PurchasePrice)
def main():
    n = input("Enter VehiclelD")
    e = input("Enter EngineSize")
    MyCar = Car(n,e)

    p = input("Enter PurchasePrice")
    MyCar.SetPurchasePrice(p)

    r = input("Enter Registration No")
    MyCar.SetRegistration(r)

    d = input("Enter DateOfRegistration")
    MyCar.SetDateOfRegistration(d)

    print("Outputting Details")
    print("VehicleID is: ",MyCar.GetVehicleID())
    print("Registration No is: ",MyCar.GetRegistration())
    print("Date0fRegistration is: ",MyCar.GetDate0fRegistration())
    print("EngineSize is: ",MyCar.GetEngineSize())
    print("PurchasePrice is: ",MyCar.GetPurchasePrice())
main()

    
