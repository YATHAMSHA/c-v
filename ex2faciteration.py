def fact(n):
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i = i + 1
    return f


n = int(input("Enter the number:"))
if n < 0:
    print("Invalid input")
elif n == 0:
    print("Factorial of 0 is 1")

else:
    f = fact(n)
    print("Factorial of {} is : {}".format(n, f))

