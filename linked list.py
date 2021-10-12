# linked list operatio
List = []
NULL = -1 # NullPointer should be set to -1 if using array element with index 0
freeptr = 0 #set starting position of free list
listptr = NULL #setting the start pointer with  null as list is initially empty

class node:# defining class to store data and pointer values
    def __init__(self):
        self.data = ""
        self.ptr = 0

def init(): #subroutine for creating a new linked list
    length = int(input("how many nodes(no of nodes) "))
    limit = length -1 
    for count in range(limit): #link all nodes to make free list
        tempNode = node() #why do we have to add this inside the loop while it could be done once before the loop
        tempNode.ptr = count+1
        List.append(tempNode)
    FinalNode = node() #last node of free list
    FinalNode.ptr = NULL
    List.append(FinalNode)
    print("number of nodes in linked list are",len(List))

    for i in range(length):
        print("node",i,"with data", List[i].data,"points to",List[i].ptr)
                                                                        
def enter(newitem):#subroutine for entering a node
    global freeptr
    global listptr
    #prevptr = 0#this line not needed#
    if freeptr != NULL:# if there is space in the array
        newptr = freeptr #take node from free list 
        List[newptr].data=newitem#store data item
        freeptr = List[newptr].ptr
        #find insertion point
        thisptr = listptr#start at beginning of list
        print("the start pointer has value: ",listptr)
        while (thisptr != NULL) and (List[thisptr].data<newitem):
            print("entered loop")
            prevptr = thisptr #remember this node
            thisptr =List[thisptr].ptr#follow the pointer to the next node
        if thisptr == listptr: # insert new node at start of list
            List[newptr].ptr = listptr
            listptr = newptr
        else: #insert new node between previous node and this node
            List[newptr].ptr = List[prevptr].ptr
            List[prevptr].ptr = newptr
        
        print("the free pointer is",freeptr)
        print("the list pointer or start is",listptr)

    for count in range(len(List)):
        print("node",count,"with data",List[count].data,"points to",List[count].ptr)

def find(item):# subroutine for finding a node
    global listptr
    
    thisptr = listptr #start at beginning of list
    while (thisptr!=NULL) and (List[thisptr].data!=item):#not end of list and item not found
        thisptr = List[thisptr].ptr #follow the pointer to the next node
    if thisptr == NULL:
        print("item not found")
    else:
        print("Item(node) found in position",thisptr)

def delete(item):# subroutine to delete a node
    global listptr
    global freeptr
    thisptr = listptr #start at beginning of list
    
    while (thisptr!=NULL) and (List[thisptr].data != item): #while not end of list and item not found
        prevptr = thisptr #remember this node
        thisptr = List[thisptr].ptr #follow the pointer to the next node
    if thisptr!=NULL: #node exists in list
        if thisptr == listptr: #first node to be deleted
            listptr = List[listptr].ptr #move start pointer to the next node in list
        else: # it is not the start node;so make the previous node’s pointer point to
              # the current node’s 'next' pointer; thereby removing all
              # references to the current pointer from the list
            List[prevptr].ptr = List[thisptr].ptr
        # updating freelist
        List[thisptr].ptr = freeptr
        freeptr=thisptr

def output():# subroutine for outputting all nodes
    global listptr
    thisptr = listptr # start at beginning of list
    while thisptr!=NULL: #while not end of list
        print(List[thisptr].data)
        thisptr=List[thisptr].ptr #follow the pointer to the next node
        
def main():
   
    init()

    choice = input("do you want to enter data into the linked list? y or n")
    if choice == "y":
        for count in range(len(List)):
            global newitem
            newitem = input("enter data")
            enter(newitem)

    choice = input("do you want to find an item in the list? y or n")
    while choice == "y":
        global item
        item = input("enter data to be found")
        find(item)
        choice = input("do you want to find more data? y or n")

    choice = input("dou you want to delete a data item from the list? y or n")
    while choice == "y":
        item = input("enter data to be deleted")
        delete(item)
        choice = input("want to delete more data? y or n")

    choice = input("do you want to output the contents of the linked list? y or n")
    if choice == "y":
        output()
    
    
main()
    
        
