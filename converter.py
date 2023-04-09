# Read today's CAD to JPY exchange rate from user
exchange_rate = float(input("Enter today's CAD to JPY exchange rate: "))

# Read CAD values to convert to JPY from user until 0 is entered as a sentinel
cad_value = float(input("Enter a CAD value to convert to JPY (or 0 to quit): "))
while cad_value != 0:
    # Convert CAD value to JPY and print the result
    jpy_value = cad_value * exchange_rate
    print(f"{cad_value} CAD is {jpy_value} JPY")
    
    # Read next CAD value to convert from user
    cad_value = float(input("Enter a CAD value to convert to JPY (or 0 to quit): "))
