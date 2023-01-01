# Script to make Tik-Tak-Toe Board of Desired Size by itteration
n = int(input("Enter the number of rows or columns: "))

def TickTakToe(n):

    for i in range(0,(n)):           # Executes n times

        for j in range(0,(n-1)):     # Executes (n-1) times

            print("_|",end ="_" )    # Constant Time - c1

        print("\n",end = "")         # Constant time - c2

    print(" | "*int(n-1),sep ="")    # Constant time - c3
    
TickTakToe(n)
