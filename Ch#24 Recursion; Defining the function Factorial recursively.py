#defining the function Factorial recursively
def factorial(n):
    if n==0:
        result = 1
    else:
        result = n * factorial(n-1)

    return result

def main():
    n = int(input("enter the number to find its factorial"))
    answer = factorial(n)
    print("factorial for ",n,"is",answer)

main()
