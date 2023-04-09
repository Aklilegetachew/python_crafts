# Read employee name, hourly rate, and hours worked from user
name = input("Enter employee name: ")
hourly_rate = float(input("Enter hourly rate: "))
hours_worked = float(input("Enter hours worked: "))

# Calculate regular pay and overtime pay (if applicable)
if hours_worked <= 160:
    regular_pay = hours_worked * hourly_rate
    overtime_pay = 0
else:
    regular_pay = 160 * hourly_rate
    overtime_pay = (hours_worked - 160) * 1.5 * hourly_rate

# Calculate total pay
total_pay = regular_pay + overtime_pay

# Print monthly paycheck
print(f"Monthly paycheck for {name}:")
print(f"Regular pay: ${round(regular_pay, 2)}")
print(f"Overtime pay: ${round(overtime_pay, 2)}")
print(f"Total pay: ${round(total_pay, 2)}")
