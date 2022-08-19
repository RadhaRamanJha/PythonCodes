# Defining lists
integer_numbers = [1,2,3,4,5]
alphabets = ["A","B","C","D","E"]
# Printing orignal list 
print("Orignal list of numbers is :" +str(integer_numbers))
print("Orignal list of alphabets is :" +str(alphabets))
# making dictonary outof above two lists using zip method
covrt = dict(zip(integer_numbers,alphabets))
# printimg the dictonary formed
print("The dictonary formed is :"+str(covrt))