# Finding factorial using recurrsion 
def recurrsion_factorial(n):
    if n == 1:
        return 1
    else:
        return(n*recurrsion_factorial(n-1))
print("99! through recurssion is "+f"{recurrsion_factorial(99)}")

# Finding Factorial using ittertion :
def itteration_factorial(n):
    result = 1
    while n >= 1:
        result = result * n
        n -= 1
    return result            
print("99! through itteration is"+f"{itteration_factorial(99)}")
print(recurrsion_factorial('hello'))

# Make it general if negative number then probable responce also consider response to string entered