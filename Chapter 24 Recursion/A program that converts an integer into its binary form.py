# a program that converts an integer into its binary form

def IntToBin(n):
    if (n==0) or (n==1):
        print(n)
    else:
        IntToBin(n//2)
        print(n % 2)
        

def main():
    n = int(input("enter number to get its binary version"))
    IntToBin(n)

main()
    
        
