m = int(input("Enter the number of columns: "))
n = int(input("Enter the number of rows: "))
for i in range(1,m+1):
    if (i==1):
        print(" X "*m)
    elif(i==m):
        print(" X "*m)
    else:
        for j in range (1,n+1):
            if(j==1):
                print(" X ",end="")
            elif(j==n):
                print(" X ",end="")
            else:
                print("   ",end="")
        print()