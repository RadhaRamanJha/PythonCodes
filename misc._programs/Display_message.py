""" 1. display_message.py """
def display_message(topic):
    print(f"I am Learing about {topic.title()} in this chapter!")

display_message("founctions")

""" 2. t-shirt_order.py """
# Defining the founction
def make_shirt(siz, msg):
    print(f"A T-shirt has to be made of {siz} size with {msg} printed on it !!")
# Calling the Fumction
make_shirt("40'", "Learn to Earn!")
make_shirt(msg="Hello Sunday", siz="Medium")
# Defining the founction Using default value
def make_shirt(siz="Large", msg="I Love Python"):
    print(f"A T-shirt has to be made of {siz} size with {msg} printed on it ..")
# Calling the founction using :-
# line 14:- Positional argument
# line 15:- Usimg Default values
# line 16 and 17:- Key word argument  
make_shirt("40'", "Learn to Earn!")
make_shirt()
make_shirt(siz="Medium")
make_shirt(siz="Medium",msg="I don't want to remain in teaching feild")

""" 3. program.py """
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

"""4. describe_city.py"""
def describe_city(city = "Nagpur", country = "India"):
    """Describes the Geo-graphic loacation of Country"""
    print(f"{city} City is in the Country {country}")

describe_city("Reykjavik","Iceland")
describe_city("Melborne","Australia")
describe_city("London","Britain")
describe_city()

"""5. global.py"""
a = 10
b = 15
c = 20
d = 25
def add():
    global a
    global b
    global c
    global d
    for a in range (10,13):
        sum = a+b+c+d
        print(a)
        print(sum)
add()
print(a)

"""6. calculation.py """
def calculation():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter Second number : "))
    add = num1+num2
    subst = num1-num2
    div = num1/num2
    print(f"The Addition of the two number is : {add}")
    print(f"The substraction of the two number is : {subst}")
    print(f"The divison of the two number is : {div}")
calculation()