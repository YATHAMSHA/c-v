def sum_and_avg_of_natural_numbers(num):
    if num == 0:
        return num
    else:
        return num + sum_and_avg_of_natural_numbers(num - 1)


number = int(input("Please Enter any Number: "))

total = sum_and_avg_of_natural_numbers(number)
average = total / number

print("The Sum of first {0} Natural Numbers  =  {1}".format(number, total))
print("Average of first {0} Natural Numbers  =  {1}".format(number, average))


