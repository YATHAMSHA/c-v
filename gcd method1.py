def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
g = gcd(a, b)
print("GCD of {} and {} is: {}".format(a, b, g))
