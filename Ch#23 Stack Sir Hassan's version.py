# Algorithm for Stack

List = []
top = 0
bottom = 0

def stack():
    global top
    global bottom
    for count in range(5):
        temp = input("enter something")
        List.append(temp)
        top = count

    print("Current condition of stack",List)
    print("Top of stack pointer is: ",top)

def pop():
    global top
    global bottom
    if top == -1:
        print("stack empty")
    else:
        List[top] = ""
        top = top-1

    print("Current condition of stack",List)
    print("Top of stack pointer is: ",top)

def push():
    global top
    global bottom
    if top == 4:
        print("Stack full")
    else:
        item = input("what to push")
        top = top + 1
        List[top] = item

    print("Current condition of stack",List)
    print("Top of stack pointer is: ",top)

def main():
    stack()
    choice = 0
    cont = "y"
    while cont == "y":
        choice = int(input("enter 1 for push 2 for pop"))
        if choice == 1:
            push()
        elif choice == 2:
            pop()
        else:
            print("invalid input")

        cont = input("continue?")

    print("Current condition of stack",List)
    print("Top of stack pointer is: ",top)


main()
            
    
    
    
        
