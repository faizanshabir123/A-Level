#programming the function Factorial iteratively, using a loop
def factorial(n):
    result = 1
    for count in range(1,n+1):
        result = result * count
    return result

def main():
    n = int(input("enter the number to find its factorial"))
    answer = factorial(n)
    print("factorial for ",n,"is",answer)
    


main()
