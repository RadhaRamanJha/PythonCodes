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