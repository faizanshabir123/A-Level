# Algorithm for Binary Search

def BinarySearch(SearchItem):
    data = [1,2,3,4,5,6,7]
    found = False
    failed = False
    first = 0
    mid = 0
    last = len(data)-1 # set boundaries of search area
    while (found == False) and (failed == False):
        mid = (first+last)//2 # find middle of current search area
        print("Current value of first is: ",first)
        print("Current value of mid   is: ",mid)
        print("Current value of last  is: ",last)
        if data[mid] == SearchItem:
            found = True
        else:
            if first >= last: # no search area left # either the start of array is reached or the end # also works with ">"alone or "="alone
                failed = True
            elif data[mid] > SearchItem: # must be in first half
                last = mid - 1 # move upper boundary
            else: # must be in second half
                first = mid + 1 # move lower boundary

    if found == True:
        print("Found at index position: ",mid) # output position where item was found
    else:
        print("Item not found")


def main():
    SearchItem = int(input("What are you searching for?"))
    BinarySearch(SearchItem)
    
                     
main()    
