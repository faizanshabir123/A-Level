class Toy:
    def __init__(self, n, i, a):
        self.__Name = n
        self.__ID = i
        self.__Price = 0.00
        self.__Min_Age = a


    def GetName(self):
        return (self.__Name)


    def GetID(self):
        return (self.__ID)


    def GetPrice(self):
        return (self.__Price)


    def GetMin_Age(self):
        return (self.__Min_Age)


    def SetPrice(self, s):
        self.__Price = s


class Game(Toy):
    def __init__(self, n, i, a, c):
        Toy.__init__(self, n, i, a)
        self.__Category = c
        self.__Console = ""


    def GetCategory(self):
        return (self.__Category)


    def GetConsole(self):
        return (self.__Console)


    def SetConsole(self, o):
        self.__Console = o


class Vehicle(Toy):
    def __init__(self, n, i, a, t, w):
        Toy.__init__(self, n, i, a)
        self.__Type = t
        self.__Weight = w


    def GetType(self):
        return (self.__Type)


    def GetWeight(self):
        return (self.__Weight)

def main():

    a, b, c, d = "","","",""
    e = 0
    f = 0.00
    Games = []
    Vehicles = []
    for count in range(1):
        c = input("enter your name")
        d = input("enter your id")
        e = int(input("enter the minimum age"))
        f = float(input("enter the price"))
        g = input("enter the vehicle type")
        h = float(input("enter the vehicle weight"))
        temp = Vehicle(c, d, e, g, h)
        temp.SetPrice(f)
        Vehicles.append(temp)

    for count in range(1):
        a = input("enter your game category")
        b = input("enter your console")
        c = input("enter your name")
        d = input("enter your id")
        e = int(input("enter the minimum age"))
        f = float(input("enter the price"))
        temp = Game(c, d, e, a)
        temp.SetPrice(f)
        temp.SetConsole(b)
        Games.append(temp)
    count = 0
    for count in range(len(Games)):
        Games[count].GetName()
        Games[count].GetID()
        Games[count].GetPrice()
        Games[count].GetMin_Age()
        Games[count].GetCategory()
        Games[count].GetConsole()
    count = 0
    for count in range(len(Vehicles)):
        Vehicles[count].GetName()
        Vehicles[count].GetID()
    
main()

