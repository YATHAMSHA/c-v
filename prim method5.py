n = int(input("Enter limit: "))

print("Prime numbers upto", n, "are:")
for num in range(2, n + 1):
    if num > 1:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=",")
