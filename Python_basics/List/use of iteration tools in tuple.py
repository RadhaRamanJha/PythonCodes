from itertools import count


tuple1 = ("Python", 1, 2, 3, "Java", "A", "B")
n = len(tuple1)
# printing alternate values of tuple
print(tuple1[0:n:2])
# printing value between index 1 to 5
print(tuple1[1:5])
# printing last value of tuple
print(tuple1[-1])
# Counting Elements of list
tuple2 = (1,2,3,4,5,6,7,8)
z= tuple2.count(3)
print(z)
#Converting above tuple in list
list2=list(tuple2)
print(list2)