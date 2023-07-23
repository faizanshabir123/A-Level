#a procedure to count down from a given integer using iteration

def CountDownFrom(n):
    for i in range(n,-1,-1):
        print(i)
    
    
def main():
    n= int(input("enter number for count down"))
    CountDownFrom(n)
    
main()
