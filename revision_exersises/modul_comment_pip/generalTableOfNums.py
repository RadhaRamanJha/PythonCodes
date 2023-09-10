"""Table of any number entered by user"""
number = int(input("Enter a number to display it's Table: "))
table_of_number = [number*i for i in range(1,11)]
print(table_of_number)