# Algorithm for Insertion Sort

def InsertionSort():
    List = [3,7,1,2,8,4,5]
    print("Original Data",List)
    for index in range(1,len(List)): # 0 index array is considered here
        ItemToBeInserted = List[index] # will be considered the first element to be inserted from unsorted part/list
        print("Currently Inserting",ItemToBeInserted,"With index: ",index,"in the unsorted part")
        Sorted = index - 1 # pointing towards first/last element of the sorted part/list
        print("Last element: ",List[Sorted],"in the sorted list is at the index: ",Sorted)
        while Sorted >= 0: # while the index has not reached the start of the array
            if ItemToBeInserted < List[Sorted]: # if the unsorted element is lesser than the element on its left
                List[Sorted + 1] = List[Sorted] # then move the first/last sorted element one position to the right
                List[Sorted] = ItemToBeInserted # ”insert” the unsorted element to the left of previous position
                Sorted = Sorted - 1 # and move one place up the array till the start of array has reached
                print("Current condition of List: ",List)
            else:
                print("No swap took place")
                print("Current condition of List: ",List)
                Sorted = Sorted - 1 # if the unsorted element is not less than the one on its left,move the pointer to the left without swapping,for next comparison 
                                    # alternatively, could have added a break here
    print("Final condition of List: ",List)


InsertionSort()
