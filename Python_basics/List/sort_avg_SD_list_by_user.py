# Accepting list from user and printing it
number_list = []
n = int(input("Enter the list size "))

print("\n")
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    number_list.append(item)
print("User list is ", sorted(number_list))
# Calculating the average of each elements of list
sum = 0 
for i in range (0,n):
    sum = sum +number_list[i]
average = sum/n
print("Average of the numbers in list is",average)
# Calculating the standard deviation of numbers entered
total_deviation_squared = 0
for i in range(0,n):
    total_deviation_squared = (total_deviation_squared + (number_list[i]-average)**2)
standard_deviation = ((total_deviation_squared))**0.5/(n-1)
print("Standarad Deviation of list elements are :",standard_deviation)
