def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


m = int(input("Enter the number to find its fibonacci: "))
for Num in range(1, m + 1):
    print(fib(Num), end=" ")
    
