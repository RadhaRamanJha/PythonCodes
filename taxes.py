income = 15000
if income<10000:
    tax_coefficient=0.0
elif income<15000:
    tax_coefficient=0.2
elif income<30000:
    tax_coefficient=0.35
elif income<100000:
    tax_coefficient=0.35
else:
    tax_coefficient=0.45
income_tax = tax_coefficient*income
# print(' i will pay:',income*tax_coefficient,'in taxes')-----1st method
print("I will pay {} in taxes".format(income_tax))  # ----formating the above result