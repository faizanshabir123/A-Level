# a procedure to count down from a given integer using recursion

def CountDownFrom(n):
    print(n)
    if n > 0:
        CountDownFrom(n-1)


def main():
    n = int(input("enter number for count down"))
    CountDownFrom(n)

main()
