def insertion_sort():
    arraydata = [99,125,121,109,115]
    print (arraydata)
    print (arraydata[0])
    numberofscores = int(5)
    for item in range(1,numberofscores):
        insertscore = arraydata[item]
        index = item - 1
        while (arraydata[index] > insertscore) and (index >=0):
            arraydata[index + 1] = arraydata[index]
            index = index -1
            
        arraydata[index + 1] = insertscore
        
    print(arraydata)    
