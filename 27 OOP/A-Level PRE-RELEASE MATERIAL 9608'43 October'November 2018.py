# A-Level PRE-RELEASE MATERIAL 9608/43 October/November 2018
# Task 1

# TASK 1.4
class Computer: # The class Computer
    def __init__(self,Code,Width,Height,Weight,Make):
        self.__Code = Code
        self.__Width = Width 
        self.__Height = Height
        self.__Weight = Weight
        self.__Make = Make
        self.__Processor = ""  
        self.__RAMSize = ""
        self.__StorageSize = ""

    # get methods
    def GetCode(self):
        return(self.__Code)
    def GetWidth(self):
        return(self.__Width)
    def GetHeight(self):
        return(self.__Height)
    def GetWeight(self):
        return(self.__Weight)
    def GetMake(self):
        return(self.__Make)
    def GetProcessor(self):
        return(self.__Processor)
    def GetRAMSize(self):
        return(self.__RAMSize)
    def GetStorageSize(self):
        return(self.__StorageSize)

    # set methods 
    def SetProcessor(self,p):
        self.__Processor = p
    def SetRAMSize(self,r):
        self.__RAMSize = r
    def SetStorageSize(self,s):
        self.__StorageSize = s

# TASK 1.5
class MobilePhone(Computer):
    def __init__(self,Code,Width,Height,Weight,Make,Camera,_3G,_4G):
        Computer.__init__(self,Code,Width,Height,Weight,Make)
        self.__Camera = Camera
        self.___3G = _3G
        self.___4G = _4G
        self.__MobilePhoneNetwork = ""

    # get methods
    def GetCamera(self):
        return(self.__Camera)
    def Get_3G(self):
        return(self.___3G)
    def Get_4G(self):
        return(self.___4G)
    def GetMobilePhoneNetwork(self):
        return(self.__MobilePhoneNetwork)
    
    # set methods
    def SetMobilePhoneNetwork(self,n):
        self.__MobilePhoneNetwork = n
        
    
class Laptop(Computer):
    def __init__(self,Code,Width,Height,Weight,Make,Touchscreen,RemovableScreen,USB3Ports):
        Computer.__init__(self,Code,Width,Height,Weight,Make)
        self.__Touchscreen = Touchscreen
        self.__RemovableScreen = RemovableScreen
        self.__TabletMode = False
        self.__USB3Ports = USB3Ports

    # get methods
    def GetTouchscreen(self):
        return(self.__Touchscreen)
    def GetRemovableScreen(self):
        return(self.__RemovableScreen)
    def GetTabletMode(self):
        return(self.__TabletMode)
    def GetUSB3Ports(self):
        return(self.__USB3Ports)

    # set methods
    def SetTabletMode(self,t):
        self.__TabletMode = t

def details():
    temp = input("Enter code for computer")
    found = False
    for i in range(len(array)):
        if array[i].GetCode() == temp:
            found = True
            break

    if found == True:
        print("Found")
    else:
        print("Not found")
       
   
array = []        
def main():
    comp1 = MobilePhone("MB1",6.2,10.8,0.3,"camphones",True,True,True)
    comp1.SetProcessor("CIE234X")
    comp1.SetRAMSize("2GB")
    comp1.SetStorageSize("6_4GB")
    comp1.SetMobilePhoneNetwork("camNetwork")
    array.append(comp1)

    comp2 = Laptop("MB2",5.9,4.5,0.5,"ciesoft",False,False,4)
    comp2.SetProcessor("ZX100")
    comp2.SetRAMSize("_4GB")
    comp2.SetStorageSize("200GB")
    comp2.SetTabletMode(False)
    array.append(comp2)
    details()

main()
    

    
    
    
    

        
        
        

