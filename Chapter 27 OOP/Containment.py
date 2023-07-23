# DECLARE Tyres:ARRAY[1:4] OF Tyre
class tyre:
    def __init__(self,n,t):
        self.__name = n
        self.__type = t


    def t_details(self):
        print(self.__name)
        print(self.__type)

class vehicle:
    def __init__(self,i,n):
        self.__vID = i
        self.__name = n
        self.__tyres = [] #this array will be of type tyre (containment)
    def setTyres (self,n):
        name = ""
        Type = ""
        name = input("enter tyre brand")
        Type = input("enter tyre type")
        
        for count in range(n):
            self.__tyres.append(tyre(name,Type))
        
    def vdetails(self):
        print(self.__vID)
        print(self.__name)
        for count in range(len(self.__tyres)):
            self.__tyres[count].t_details()


def main():
    VID = input("enter v_ID")
    NAME = input("enter v_NAME")
    MyTruck = vehicle(VID,NAME)
    number_of_tyres = 0
    number_of_tyres = int(input("enter number of tyres"))
    
    MyTruck.setTyres(number_of_tyres)
    print("printing details")
    MyTruck.vdetails()
    
main()
