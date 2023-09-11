# Basic income tax neglecting the deduction and surcharges
annual_income = int(input("Enter your annual income: "))
if (annual_income in range (250001,500000)):
    slab_tax = 5*(annual_income-250000)/100
    monthly_tax = slab_tax/12
    print(f"Income tax to be paid monthly is {monthly_tax}")
elif (annual_income in range(500001,750000)):
    slab_tax = 12500 + 10*(annual_income-500000)/100
    monthly_tax = slab_tax/12
    print(f"Income tax to be paid monthly is {monthly_tax}")
elif (annual_income in range(750001,1000000)):
    slab_tax = 37500 + 15*(annual_income-750000)/100
    monthly_tax = slab_tax/12
    print(f"Income tax to be paid monthly is {monthly_tax}")
elif (annual_income in range(1000001,1250000)):
    slab_tax = 75000 + 20*(annual_income-100000)/100
    monthly_tax = slab_tax/12
    print(f"Income tax to be paid monthly is {monthly_tax}")
elif (annual_income in range(1250001,1500000)):
    slab_tax = 125000 + 25*(annual_income-100000)/100
    monthly_tax = slab_tax/12
    print(f"Income tax to be paid monthly is {monthly_tax}")
elif (annual_income > 1500000):
    slab_tax = 187500 + 30*(annual_income-150000)/100
    monthly_tax = slab_tax/12
    print(f"Income tax to be paid monthly is {monthly_tax}")
else:
    print("You donot need to pay any income tax")