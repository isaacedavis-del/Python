while True:
    try:
        income = float(input("Enter the annual income: "))
        if income >= 0:
            break
        print("Income must be a positive number, please try again.")
    except ValueError:
        print("Invalid input, please enter a number")

tax_boundary = 85528

if income <= tax_boundary:
    tax = 0.18*income-556.02
else:
    tax = 14839.02+(income-tax_boundary)*0.32
    
tax = max(tax,0)
tax = round(tax, 0)
print("The tax is:", tax, "thalers")