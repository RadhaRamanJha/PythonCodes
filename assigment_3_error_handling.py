from distutils.log import error
from re import A
from tokenize import String

# Defining Founction to check:- 
# Type of Data Entered by the user
def check_entry(a):
    try:
        int(a) == True
        print(f"{a} is an integer" )
    except:
        try:
            float(a) == True
            print(f"{a} is an float")
        except:
            str(a) == True
            print(f"{a} is a string")
# Taking the input from user
A = input("Do the First Entry :")
B = input("Do the Second Entry :")

# Check for the type of data entered by the user
check_entry(A)
check_entry(B)

# using try-expect-finaly(try-expect-else block)block 
# to perform the desired operation
try:
    int(A)==int(B)==True
    sum = int(A)+int(B)
except:
    ValueError
    print("Not possible to add these two values")
    pass
finally:
    try:
        int(A)==int(B)==True
        print(f"The Summation of both numbers is {sum}")
    except:
        ValueError
        print(f"{A}\t {B}")
    else:
        print("Press <CTRL+F5> to try again")