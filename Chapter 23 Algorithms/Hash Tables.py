# operations for hash table
hashtable = [] 

class customer: # class for customer data
    def __init__(self):
        self.customerID = "empty"
        self.name = "empty"
        self.age = "empty"

def hashval(KeyField): # subroutine to calculate index using a key field
    address = (int(KeyField)) % (len(hashtable))
    return address

def insert(newrecord): # subroutine to insert a record into a hash table
    KeyField = newrecord.customerID
    index = hashval(KeyField) # calculating index using key field
    
    while hashtable[index].customerID != "empty": # repeat until empty slot is found
        index = index +1 # go to next slot to check if empty
        if index > maxx: # beyond table boundary?
            index = 0 # wrap around to beginning of table
            
    hashtable[index].customerID = newrecord.customerID
    hashtable[index].name = newrecord.name
    hashtable[index].age = newrecord.age

def FindRecord(KeyField): # subroutine to find a record in a hash table
    index = hashval(KeyField) # calculating index using key field
    startIndex = index 
    while (hashtable[index].customerID != KeyField) and (hashtable[index].customerID != "empty"):
        index = index+1 # go to next slot
        if index > maxx: # beyond table boundary?
            index = 0 # wrap around to beginning of table
        if index == startIndex: 
            break
 
    if hashtable[index].customerID == KeyField : # if record found #book had other statement: (hashtable[index].customerID != "empty")
        return hashtable[index] # return the record
    else:
        return -1

def main():
    size = int(input("what do you want the length of the hashtable to be"))
    for i in range(size):
        hashtable.append(customer())
        
    global maxx
    maxx = len(hashtable)-1

    for i in range(len(hashtable)):
        print("customer id",hashtable[i].customerID,"customer name",hashtable[i].name,"customer age",hashtable[i].age)

    choice= input("do you want to add records into the hashtable? y or n")
    if choice == "y":
        for j in range(len(hashtable)):
            newrecord = customer()
            newrecord.customerID = input("enter customer ID")
            newrecord.name = input("enter name")
            newrecord.age = input("enter age")
            insert(newrecord)
            for i in range(len(hashtable)):
                print("customer id",hashtable[i].customerID,"customer name",hashtable[i].name,"customer age",hashtable[i].age)

            choice = input("want to enter more data")
            if choice!="y":
                break
        
    choice = input("do you want to find a record? y or n")
    while choice == "y":
        KeyField = input("enter the customer id")
        result = FindRecord(KeyField)
        if result == -1:
            print("not found")
        else:
            print("customer id: ",result.customerID,"name is: ",result.name,"age is: ",result.age)
        choice = input("Want to find more records? y or n")
            
            
main()    
          
