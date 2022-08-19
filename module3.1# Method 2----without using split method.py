# Method 2----without using split method 
number_list = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i)
# Python input() function always converts the user input into a string then returns it to the calling program
# with this in mind we convert each element usinmg int() functiom
    item = int(input())
    number_list.append(item)
print("User list is ", number_list)
for i in range (len(number_list)):
    print(number_list[i])
