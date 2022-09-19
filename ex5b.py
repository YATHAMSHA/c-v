overtime_pay = overtime_pay_total = 0
for i in range(1, 11):
    time_worked = int(input(f"Enter the time employee {i} worked in hr: "))
    if time_worked > 40:
        over_time = time_worked - 40
        overtime_pay = 12 * over_time
        print(f"Overtime Pay Of employees {i} is", overtime_pay)
        overtime_pay_total += overtime_pay
    else:
        print(f"Overtime Pay Of employees {i} is 0")

print("\nTotal Overtime Pay Of 10 Employees is", overtime_pay_total)

