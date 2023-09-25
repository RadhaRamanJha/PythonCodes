# Using reccurssion
def reccurssion_Sum_sqaured(n):
    if n == 0:
       return 0
    else:
       return(n**2+reccurssion_Sum_sqaured(n-1))
print('The sum of first 3 natural numbers using reccurssion is '+f"{reccurssion_Sum_sqaured(3)}")

# Using itteration
n = int(input("Enter a natural number: "))
result = 0
while n>0:
    result += n**2
    n -=1
print(f"The sum of squares of natural numbers upto entered one using itteration method is {result}")

# Make it general if negative number then probable responce also consider response to string entered