# Error Handling through else block
num1 = int(input("Enter The First Number :"))
num2 = int(input("Enter the Second number :"))
try:
    num3 = num1/num2
except:
    ZeroDivisionError
    print(f"{num2} being denominator, cannot take a nil value")
    print("Division by 0 not possible")

else:
    print(f"The division of {num1} and {num2} results {num3}")