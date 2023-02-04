n = int(input("Enter the maximum number of stars per line: "))
for i in range (0,n+1):
    j = n-i
    print(" "*j, end= "")
    print("*"*i)