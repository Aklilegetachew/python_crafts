def calculate_assistance(income, num_children):
    if income >= 40000 and income <= 50000 and num_children >= 3:
        return 1200 * num_children
    elif income >= 30000 and income < 40000 and num_children >= 2:
        return 1700 * num_children
    elif income < 30000:
        return 2100 * num_children
    else:
        return 0

# Read household income and number of children from user until -1 is entered as a sentinel
income = float(input("Enter the household income (or -1 to quit): "))
while income != -1:
    num_children = int(input("Enter the number of children: "))
    assistance_amount = calculate_assistance(income, num_children)
    print(f"The financial assistance amount is ${assistance_amount}")
    income = float(input("Enter the household income (or -1 to quit): "))
