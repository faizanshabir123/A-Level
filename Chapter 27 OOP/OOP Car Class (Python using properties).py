# ch 27 OPP
# Python using properties
class Car:
    def __init__(self, n, e):      # constructor
        self.__VehicleID = n
        self.__Registration = ""
        self.__DateOfRegistration = None
        self.__EngineSize = e
        self.__PurchasePrice = 0.00

    @property
    def VehicleID(self):
        return(self.__VehicleID)

    @property
    def EngineSize(self):
        return(self.__EngineSize)

    @property
    def Registration(self):
        return(self.__Registration)
    @Registration.setter
    def Registration(self, r):
        self.__Registration = r

    @property
    def DateOfRegistration(self):
        return(self.__DateOfRegistration)
    @DateOfRegistration.setter
    def DateOfRegistration(self, d):
        self.__DateOfRegistration = d

    @property
    def PurchasePrice(self):
        return(self.__PurchasePrice)
    @PurchasePrice.setter
    def PurchasePrice(self, p):
        self.__PurchasePrice = p

def main():
    n = input("Enter VehiclelD")
    e = input("Enter EngineSize")
    MyCar = Car(n,e)

    p = input("Enter PurchasePrice")
    MyCar.PurchasePrice = p

    r = input("Enter Registration No")
    MyCar.Registration = r

    d = input("Enter DateOfRegistration")
    MyCar.DateOfRegistration = d

    print("Outputting Details")
    print("VehicleID is: ",MyCar.VehicleID)
    print("Registration No is: ",MyCar.Registration)
    print("Date0fRegistration is: ",MyCar.DateOfRegistration)
    print("EngineSize is: ",MyCar.EngineSize)
    print("PurchasePrice is: ",MyCar.PurchasePrice)
main()
