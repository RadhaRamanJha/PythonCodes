# if comma is not placed after first element it is considered as a string in python
tuple = ("python")*3
print(tuple)
# first element should be seperated by comma to tell python it is tuple
tuple = ("python",)*3
print(tuple)
# finding length in tuple
tuple1 = ("Python", 1, 2, 3, "Java", "A", "B")
n = len(tuple1)

# Slicing in tuple
# printing alternate values of tuple
print(tuple1[0:n:2])
# printing value between index 1 to 5
print(tuple1[1:5])
# printing last value of tuple
print(tuple1[-1])
