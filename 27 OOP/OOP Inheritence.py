#Vehicle
##Vehicle ID STRING
##EngineType STRING
##OwnerName STRING
##
##TRUCK
##MaxLoad
##Car
##MaxPassengers




class Vehicle:
    def __init__(self,vid,e):
        self.__vehicleId = vid
        self.__engineType = e
        self.__owner = ""
        
    def setowner(self,o):
        self.__owner = o
    def getowner(self):
        return(self.__owner)
    def getengine(self):
        return(self.__engineType)
    def getvid(self):
        return(self.__vehicleId)
    def printdetails(self):
        print(self.__vehicleId," ",self.__engineType," ",self.__owner)
class Truck(Vehicle):
    def __init__(self,vid,e):
        Vehicle.__init__(self,vid,e)
        self.__maxload = 0

    def setmaxload(self,l):
        self.__maxload = l
    def getmaxload(self):
        return(self.__maxload)
class Car(Vehicle):
    def __init__(self,vid,e):
        Vehicle.__init__(self,vid,e)
        self.__maxpass = 0
    def setpass(self,p):
        self.__maxpass = p
    def getpass(self):
        return(self.__maxpass)
    #polymorphism
    def printdetails(self):
        Vehicle.printdetails(self)
        e_type = ""
        e_type = self.getengine()
        if e_type == "hybrid" or e_type == "electric":
            print("You are eligible for green discount on tax")
        else:
            print("not green discount on tax")
        
        


    
def main():
    choice = 0
    choice = int(input("Enter 1 for Truck and 2 for Car"))
    v_id = ""
    v_engine = ""
    if choice == 1:
        print("Print you have chosen truck object")
        v_id = input("enter your truck id")
        v_engine = input("enter your engine")
        MyTruck = Truck(v_id,v_engine)
        max_load = 0
        owner = ""
        max_load = int(input("enter the max load"))
        owner = input("Enter the owner name")
        MyTruck.setowner(owner)
        MyTruck.setmaxload(max_load)
        print("owner of truck ",MyTruck.getowner())
        print("engine type ", MyTruck.getengine())
        print("the vehicle id ",MyTruck.getvid())
        print("the max load for this truck ",MyTruck.getmaxload())
        MyTruck.printdetails()
    else:
        print("Print you have chosen car object")
        v_id = input("enter your car id")
        v_engine = input("enter your engine")
        MyCar = Car(v_id,v_engine)
        max_pass = 0
        owner = ""
        max_pass = int(input("enter the max number of passangers"))
        owner = input("Enter the owner name")
        MyCar.setowner(owner)
        MyCar.setpass(max_pass)
        print("owner of Car ",MyCar.getowner())
        print("engine type ", MyCar.getengine())
        print("the vehicle id ",MyCar.getvid())
        print("the max passengers for this car ",MyCar.getpass())
        MyCar.printdetails()

main()
        
        
        
       
