lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=",")

