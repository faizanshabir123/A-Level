# Algorithm for Stacks

EMPTYSTRING = "" # Constant
NullPointer = -1 # Constant # NullPointer should be set to -1 if using array element with index 0
MaxStackSize = 8
Stack = []

def InitialiseStack():
    global BaseOfStackPointer
    global TopOfStackPointer
    global Stack
    print("Initialising the stack")
    Stack = [""]*MaxStackSize
    BaseOfStackPointer = 0 # set base of stack pointer
    TopOfStackPointer = NullPointer # set top of stack pointer
    print("Current condition of stack",Stack)
    print("Top of stack pointer is: ",TopOfStackPointer)
    
def Push(NewItem):
    global BaseOfStackPointer
    global TopOfStackPointer
    global Stack
    if TopOfStackPointer < MaxStackSize - 1: # there is space on the stack
        TopOfStackPointer = TopOfStackPointer + 1 # increment top of stack pointer
        Stack[TopOfStackPointer] = NewItem # add item to top of stack
    else:
        print("Stack full")

    print("Current condition of stack",Stack)
    print("Top of stack pointer is: ",TopOfStackPointer)

def Pop():
    global BaseOfStackPointer
    global TopOfStackPointer
    global Stack
    Item = -1
    if TopOfStackPointer > NullPointer: # there is at least one item on the stack
        Item = Stack[TopOfStackPointer]
        Stack[TopOfStackPointer] = EMPTYSTRING # pop item off the top of the stack
        TopOfStackPointer = TopOfStackPointer - 1 # decrement top of stack pointer

    return Item

def main():
    InitialiseStack()
    cont = "y"
    while cont == "y":
        choice = int(input("enter 1 for push 2 for pop"))
        if choice == 1:
            NewItem = input("what to push")
            Push(NewItem)
        elif choice == 2:
            ItemPopped = Pop()
            if ItemPopped == -1:
                print("Stack Empty")
            else:
                print("Item popped is: ",ItemPopped)
            print("Current condition of stack",Stack)
            print("Top of stack pointer is: ",TopOfStackPointer)
        else:
            print("invalid input")

        cont = input("continue?")

main()
        
        
    
            
            
            
    
    
    
        
        
    
    
    
    
    
    


