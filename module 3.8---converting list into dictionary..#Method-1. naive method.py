# Defining lists
integer_numbers = [1,2,3,4,5]
alphabets = ["A","B","C","D","E"]
#defining empty dictonary
conv = {}
print("Orignal list of integer numbers is :" +str(integer_numbers))
print("Orignal list of alphabets is :" +str(alphabets))
# allocating key:value pair of 'conv' using "Naive method"
for integer_number in integer_numbers:
    for alphabet in alphabets:
        conv[integer_number]=alphabet
        print(alphabet)
        alphabets.remove(alphabet)
        print("Orignal list of alphabets is :" +str(alphabets))
    print(str(integer_number),str(conv))
    #    break
# Printing the resultant Dictionary
print("Resultant Dictionary is :" +str(conv))