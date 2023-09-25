# To Check the entry is a string or not
# we need to eliminate all possible cases
# as every input is considered as string 
entry = input("Enter a String and press enter :")
# Eliminating the possiblity of 1. integer
try:
    int(entry)==True
    print(f"{entry} is an integer please enter a String")
except:
# Eliminating the possiblty of 2. Float
    try:
        float(entry)==True
        print(f"{entry} is a Float please enter a String")
    except:
# Check for String
        str(entry)==True
        print(f"{entry} is a String. Have a nice day !!")