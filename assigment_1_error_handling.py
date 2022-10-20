# To Check wether an input is integer or not 
user_input1 = input("Enter a Number :")
user_input2 = input("Enter one more number :")

# Method 1 :- By using try and expect method
try:
    int(user_input1) == True
    print(f"{user_input1} is an integer")
except:
    print(f"{user_input1} is not an integer")
try:
    int(user_input2) == True
    print(f"{user_input2} is an integer ")
except:
    print(f"{user_input2} is not an integer")

# Method2:-By using 'isnumeric()' or 'isdigit()'; limitation - both will read negative integer as String
print(f"{user_input1} is an integer ?")
print(user_input1.isnumeric())
print(f"{user_input2} is integer ?")
print(user_input2.isdigit())