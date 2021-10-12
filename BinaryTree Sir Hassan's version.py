NULL = -1
BT = []
root = 0
free = 0
class node:
    def __init__(self):
        self.data = 0
        self.left = 0
        self.right = 0
    
        
def initialise(number):
    global root
    global free
    for count in range(number):
        newnode = node()
        newnode.left = count+1
        newnode.right = -1
        BT.append(newnode)
    BT[number-1].left = NULL
    root = NULL
    free = 0
def insert(newdata):
    global root
    global free
    newnode = 0
    thisnode = 0
    prevnode = 0
    left=False 
    if free != NULL:
        newnode = free
        free = BT[newnode].left
        BT[newnode].data = newdata
        BT[newnode].left = NULL
        BT[newnode].right = NULL
        if root == NULL:
            root = newnode
        else:
            thisnode = root
            while thisnode != NULL:
                prevnode = thisnode
                if BT[thisnode].data>newdata:
                    left = True
                    thisnode = BT[thisnode].left
                else:
                    left = False
                    thisnode = BT[thisnode].right
            if left == True:
                BT[prevnode].left = newnode
            else:
                BT[prevnode].right = newnode


def traverse(root):
    if root!=NULL:
        print("the root(data) is ",BT[root].data)
        traverse(BT[root].left)
        print(BT[root].data)
        traverse(BT[root].right)
        print("the printing sequence with ",BT[root].data," as root ends here")
    

def main():
    initialise(5)
    print(root,free)
    for count in range(len(BT)):
        print(BT[count].left, BT[count].data, BT[count].right)
    newdata = 0
    cont = "Y"
    while free!=NULL:
        newdata = int(input("Enter New Value"))
        insert(newdata)
        print (root,free)
    
        
    for count in range(len(BT)):
        print("node number: ",count," left pointer: ",BT[count].left," Data:  ",BT[count].data," right pointer: ", BT[count].right)
    print("In Order Tree Traversal") 
    traverse(root)  
    
        
main()                  
    
    
