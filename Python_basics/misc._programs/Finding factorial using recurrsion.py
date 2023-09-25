# Finding factorial using recurrsion 
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return(n*factorial(n-1))
# print(factorial(5))

# Finding Factorial using intertion :
def factorial(n):
    for n in range(n,0,-1):
        return(n*n-1)
print(factorial(5))