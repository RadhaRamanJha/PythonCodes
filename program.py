x = input("Enter The First input :")
y = input("Enter The Second input :")
if type(x):
    print("Both the value should be of same type")
if type(int(x))==type(int(y))==int:
    if (int(x)*int(y))>=0:
        print(int(x)*int(y))
    else:
        print(int(x)+int(y))
elif type(x)==type(y)==str:
    print(x.upper()+y.upper())
