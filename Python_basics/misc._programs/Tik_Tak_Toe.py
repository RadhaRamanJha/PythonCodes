# Script to make Tik-Tak-Toe Board of Desired Size by itteration
# n = int(input("Enter the number of rows or columns: "))

# def TickTakToe(n):

#     for i in range(0,(n)):           # Executes n times

#         for j in range(0,(n-1)):     # Executes (n-1) times

#             print("_|",end ="_" )    # Constant Time - c1

#         print("\n",end = "")         # Constant time - c2

#     print(" | "*int(n-1),sep ="")    # Constant time - c3
    
# # TickTakToe(n)
# maxlist  = [1,5,5,5,5,1]
# max = maxlist[0]
# indeOfMax = 0
# for i in range (1,len(maxlist)):
#     if maxlist[i] > max :
#         indeOfMax = i
#         max = maxlist[i]
# print(indeOfMax)

vegies = ['carrot','bo','potato','asp']
vegies.insert(vegies.index('bo'),"cerely")
print(vegies)
tup1 = (12,13,14,15)
print( max(tup1) )
print(min(tup1))
print(list(tup1))
numbers = {}
letters = {}
combs = {}
numbers[1] = 56
numbers[3] = 7
letters[4] = 8
combs['Numbers'] = numbers
combs['Letters'] = letters
print(combs)
a = {}
a['a'] = 1
a['b'] = [2,3,4]
print(a)