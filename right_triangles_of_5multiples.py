n = int(input("Enter the maximum number of multiples to display per line: "))
for i in range(1,n+2):
    for j in range(1,i):
        print(5*j,end="  ")
    print()