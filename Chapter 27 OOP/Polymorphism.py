class vehicle:
    def __init__(self,i,n):
        self.__vid = i
        self.__name = n

    def getdetails(self):
        print(self.__vid)
        print(self.__name)



class car(vehicle):
    def __init__(self,i,n,p):
        vehicle.__init__(self,i,n)
        self.__pass = p

    def getdetails(self):
        print("These are car details only")
        vehicle.getdetails(self)
        print(self.__pass)

class truck(vehicle):
    def __init__(self,i,n,w):
        vehicle. __init__(self,i,n)
        self.__maxwt = w
    def getwt(self,x):
        return(self.__maxwt)


def main():
    ID = ""
    name = ""
    passengers = 0
    ID = input("enter car ID")
    name = input("enter car name")
    passengers = int(input("enter the number of passangers"))
    Car = car(ID,name,passengers)
    ID = input("enter TRUCK ID")
    name = input("enter TRUCK name")
    wt = int(input("enter max weight"))
    Truck = truck(ID,name,wt)
    #testing polymorphism
    Car.getdetails()
    Truck.getdetails()

main()
