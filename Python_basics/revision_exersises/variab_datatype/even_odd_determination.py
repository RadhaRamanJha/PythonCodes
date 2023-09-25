a = int(input("Enter a number : " ))
b = a % 2
if b == 0 :
    print ("The number {} is even".format(a))
else:
    print("The number {} is odd".format(a))
# list play
cubes = list(value**3 for value in range(1,101,2))
print(cubes[11:22:2])
