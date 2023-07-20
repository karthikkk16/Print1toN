def printN(n):
    if n>=1:
        printN(n-1)
        print(n,end=" ")
    return "\n"
n=int(input())
print(printN(n))