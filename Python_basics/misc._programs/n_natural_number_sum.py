# Finding Sum of n natural number using recurssion

def recurssion_sum(n):
    if n==0:
       return 0
    else:
        return(n+recurssion_sum(n-1))
print("The sum of natural numbers upto 99 using recurssion is " + f"{recurssion_sum(99)}")

# Finding Sum of n natural number using iteration

def iteration_sum(n):
    result = 0
    for n in range(1,n+1):
        result+=n
    return(result)
print("The sum of natural numbers upto 99 using iteration is " +f"{iteration_sum(99)}")

# Make it general if negative number then probable responce also consider response to string entered