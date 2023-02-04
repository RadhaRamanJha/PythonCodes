n = int(input("Enter the maximum integer to print: "))
for i in range(0,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j, end="")
    print()