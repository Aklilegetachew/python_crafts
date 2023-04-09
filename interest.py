# Read initial balance and annual interest rate from user
initial_balance = float(input("Enter your initial balance: "))
annual_interest_rate = float(
    input("Enter the annual interest rate as a percentage: "))

# Calculate monthly interest rate and number of months
monthly_interest_rate = annual_interest_rate / 12 / 100
num_months = 4

# Calculate balance after each month with monthly compounding
balance = initial_balance
for month in range(1, num_months+1):
    interest = balance * monthly_interest_rate
    balance = balance + interest
    print(f"Balance after month {month}: {round(balance, 2)}")

# Print the balance after the fourth month
print("Your balance after the first four months is:", round(balance, 2))
