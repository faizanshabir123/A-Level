# Binary tree operations
tree = []
NULL = -1 # NullPointer should be set to -1 if using array element with index 0
rootptr = 0
freeptr = 0

class node: # class to store data and pointers
    def __init__(self):
        self.data = ""
        self.rightptr = -1
        self.leftptr = 0

def newtree(): # subroutine to create a new binary tree
    global rootptr
    global freeptr
    rootptr = NULL # set start pointer
    freeptr = 0 # set starting position of free list
    length = int(input("how many nodes(no of nodes) "))
    limit = length -1
    for count in range(limit): # link all nodes to make free list
        tempNode = node()
        tempNode.leftptr = count+1
        tree.append(tempNode)
    FinalNode = node()
    FinalNode.leftptr = NULL # last node of free list
    tree.append(FinalNode)
    print("number of nodes in binary tree are",len(tree))

    for i in range(length):
        print("left pointer: ",tree[i].leftptr,"node number ",i,"right pointer: ",tree[i].rightptr)

def insertnode(newitem): # subroutine to Insert a new node into a binary tree
    global rootptr
    global freeptr
    turnedleft = False
    if freeptr!= NULL: # there is space in the array
        newnodeptr = freeptr # take node from free list
        freeptr = tree[newnodeptr].leftptr # updating free pointer
        tree[newnodeptr].data = newitem # store data item
        tree[newnodeptr].leftptr = NULL # set null pointers
        tree[newnodeptr].rightptr = NULL # set null pointers
        if rootptr == NULL: # check if empty tree
            rootptr = newnodeptr # insert new node at root
        else: # find insertion point
            thisnodeptr = rootptr # start at the root of the tree
            while thisnodeptr!= NULL: # while not a leaf node
                prevnodeptr = thisnodeptr # remember this node
                if tree[thisnodeptr].data > newitem: # follow left pointer
                    turnedleft = True
                    thisnodeptr = tree[thisnodeptr].leftptr
                else: # follow right pointer
                    turnedleft = False
                    thisnodeptr = tree[thisnodeptr].rightptr

            if turnedleft == True:
                tree[prevnodeptr].leftptr = newnodeptr
            else:
                tree[prevnodeptr].rightptr = newnodeptr
            print("start pointer is: ",rootptr)    
            print("the free pointer is",freeptr)
        for count in range(len(tree)):
            print("node number",count,"left pointer: ",tree[count].leftptr,"data",tree[count].data,"right pointer: ",tree[count].rightptr)


# subroutine to find a node in a binary tree
def find(searcheditem): # this function returns pointer to the node in which data is found/located
    global rootptr
    thisnodeptr = rootptr # start at the root of the tree
    while (thisnodeptr!= NULL) and (tree[thisnodeptr].data!= searcheditem): # while a pointer to follow and search item not found
        if tree[thisnodeptr].data > searcheditem: # follow left pointer
            thisnodeptr = tree[thisnodeptr].leftptr
        else: # follow right pointer
            thisnodeptr = tree[thisnodeptr].rightptr
    return thisnodeptr # will return null pointer if search item not found

# most probably traversal is not in syllabus
def traverse(rootptr): # subroutine for InOrder Tree Traversal and its output
    if rootptr!= NULL: # if this becomes false then it will be the base case otherwise it will be the general case
        print("the data at the current root(node) is: ",tree[rootptr].data) # outputs the data value of the root node of the sub tree/whole tree which will now be traversed
        traverse(tree[rootptr].leftptr) # First recur on left child
        print(tree[rootptr].data) # then print the data of node
        traverse(tree[rootptr].rightptr) # now recur on right child
        print("the printing sequence with ",tree[rootptr].data," as root ends here") # outputs the data value of the root node of the sub tree/whole tree
                                                                                     # which has completely been output/printed
        

def main():
    newtree()

    choice = input("do you want to enter data into the linked list? y or n")
    if choice == "y":
        for count in range(len(tree)):
            global newitem
            newitem = input("enter data")
            insertnode(newitem)
            
        
    choice = input("do you want to find an item in the list? y or n")
    while choice == "y":
        global searcheditem
        searcheditem = input("enter data to be found")
        result = find(searcheditem)
        if result == NULL:
            print("not found",result)
        else:
            print("found at node number: ",result)

        choice = input("do you want to find more data? y or n")



    choice = input("do you want to output the binary tree? y or n")
    if choice == "y":
        print("InOrder Tree Traversal")
        traverse(rootptr)
        
                                         


main()

                    
                    
        
    
