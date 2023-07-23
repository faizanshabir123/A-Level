# Algorithm for Queues

List = []
front = 0
end = 0

def queue():
    global front
    global end
    for count in range(5):
        temp = input("enter something")
        List.append(temp)
        end = count

    print("Current condition of Queue: ",List)
    print("The Front of Queue Pointer is: ",front)
    print("The End of Queue Pointer is: ",end)

def leaveQ():
    global front
    global end
    if front == end:
        print("queue is empty")
    elif (front == 4):   #and (end != 0):
        List[front] = ""
        front = 0
    else:
        List[front] = ""
        front = front + 1

    print("Current condition of Queue: ",List)
    print("The Front of Queue Pointer is: ",front)
    print("The End of Queue Pointer is: ",end)

def enterQ(item):
    global front
    global end
    if (end == 4 and front == 0) or (end+1 == front):
        print("Queue full")
    elif end == 4:
        end = 0
        List[end] = item
    else:
        end = end + 1
        List[end] = item
    
    print("Current condition of Queue: ",List)
    print("The Front of Queue Pointer is: ",front)
    print("The End of Queue Pointer is: ",end)

def main():
    queue()
    cont = "y"
    while cont == "y":
        choice = int(input("1 to enterQ 2 to leavQ"))
        if choice == 1:
            temp = input("enter something")
            enterQ(temp)
        elif choice == 2:
            leaveQ()
        else:
            print("invalid option")

        cont = input("continue?")

    print("Current condition of Queue: ",List)
    print("The Front of Queue Pointer is: ",front)
    print("The End of Queue Pointer is: ",end)

main()

    
            
            
    

    
        
        
        
        
    
    
    
    
