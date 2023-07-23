# Algorithm for Insertion Sort

def InsertionSort():
    List = [3,7,1,2,8,4,5]
    print("Original Data",List)
    for index in range(1,len(List)): # 0 index array is considered here
        ItemToBeInserted = List[index] # will be considered the first element to be inserted from unsorted part/list
        print("Currently Inserting",ItemToBeInserted,"With index: ",index,"in the unsorted part")
        Sorted = index - 1 # pointing towards first/last element of the sorted part/list
        print("Last element: ",List[Sorted],"in the sorted list is at the index: ",Sorted)
        while (ItemToBeInserted < List[Sorted]) and (Sorted > -1): # will exist when either the place for the item is found or the start of the array is reached
            List[Sorted + 1] = List[Sorted] # move the first/last sorted element one position to the right
            Sorted = Sorted - 1 # and move one place up the array till the start of array has reached
            print("Current condition of List:(inside loop) ",List)

        List[Sorted + 1] = ItemToBeInserted # insert item
        print("Current condition of List:(outside loop) ",List)

    print("Final condition of List: ",List)


InsertionSort()            
        
 
