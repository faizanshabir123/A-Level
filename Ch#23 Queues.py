# Algorithm for Queue

EMPTYSTRING = "" # Constant
NullPointer = -1 # Constant # NullPointer should be set to -1 if using array element with index 0
MaxQueueSize = 5
Queue = []

def InitialiseQueue():
    global FrontOfQueuePointer
    global EndOfQueuePointer
    global NumberInQueue
    global Queue
    print("Initialising the Queue")
    Queue = [""]*MaxQueueSize
    FrontOfQueuePointer = 0 # set front of queue pointer
    EndOfQueuePointer = NullPointer # set end of queue pointer
    NumberInQueue = 0 # no elements in queue
    print("Current condition of Queue",Queue)
    print("Front Of Queue Pointer is: ",FrontOfQueuePointer)
    print("End Of Queue Pointer is: ",EndOfQueuePointer)
    print("Number of items in Queue: ",NumberInQueue)

def AddToQueue(NewItem):
    global FrontOfQueuePointer
    global EndOfQueuePointer
    global NumberInQueue
    global Queue
    if NumberInQueue < MaxQueueSize: # there is space in the queue
        EndOfQueuePointer = EndOfQueuePointer + 1 # increment end of queue pointer

        if EndOfQueuePointer > MaxQueueSize - 1: # check for wrap-round
            EndOfQueuePointer = 0 # wrap to beginning of array

        Queue[EndOfQueuePointer] = NewItem # add item to end of queue
        NumberInQueue = NumberInQueue + 1 # increment counter
    else:
        print("Queue is Full")

    print("Current condition of Queue",Queue)
    print("Front Of Queue Pointer is: ",FrontOfQueuePointer)
    print("End Of Queue Pointer is: ",EndOfQueuePointer)
    print("Number of items in Queue: ",NumberInQueue)

def RemoveFromQueue():
    global FrontOfQueuePointer
    global EndOfQueuePointer
    global NumberInQueue
    global Queue
    Item = NullPointer
    if NumberInQueue > 0: # there is at least one item in the queue
        Item = Queue[FrontOfQueuePointer]
        Queue[FrontOfQueuePointer] = EMPTYSTRING # remove item from the front of the queue
        NumberInQueue = NumberInQueue - 1

        if NumberInQueue == 0: # if queue empty, reset pointers
            InitialiseQueue()
        else:
            FrontOfQueuePointer = FrontOfQueuePointer + 1 # increment front of queue pointer

            if FrontOfQueuePointer > MaxQueueSize - 1: # check for wrap-round
                FrontOfQueuePointer = 0 # wrap to beginning of array

    return Item

def main():
    InitialiseQueue()
    cont = "y"
    while cont == "y":
        choice = int(input("enter 1 to AddToQueue  2 to RemoveFromQueue"))
        if choice == 1:
            NewItem = input("what to add")
            AddToQueue(NewItem)
        elif choice == 2:
            ItemRemoved = RemoveFromQueue()
            if ItemRemoved == NullPointer:
                print("Queue Empty")
            else:
                print("Item removed is: ",ItemRemoved)

            print("Current condition of Queue",Queue)
            print("Front Of Queue Pointer is: ",FrontOfQueuePointer)
            print("End Of Queue Pointer is: ",EndOfQueuePointer)
            print("Number of items in Queue: ",NumberInQueue)
        else:
            print("invalid input")

        cont = input("continue?")

main()
            
            
    
            

        
    

    
    
