# a procedure to count up to a given integer using recursion

def CountUpTo(n):
    if n > 0:
        CountUpTo(n-1)

    print(n)

def main():
    n = int(input("enter number to count up to"))
    CountUpTo(n)

main()
        
