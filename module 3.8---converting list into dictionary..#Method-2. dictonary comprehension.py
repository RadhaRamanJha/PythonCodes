# Defining lists
integer_numbers = [1,2,3,4,5]
alphabets = ["A","B","C","D","E"]
# Printing orignal list 
print("Orignal list of numbers is :" +str(integer_numbers))
print("Orignal list of alphabets is :" +str(alphabets))
# Creating dictonary out of above two lists using dictionary comprehension
covrt = {integer_numbers[i]:alphabets[i] for i in range(len(integer_numbers))}
#printing dictonary
print(covrt)