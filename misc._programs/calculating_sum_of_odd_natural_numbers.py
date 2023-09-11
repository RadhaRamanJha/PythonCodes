# calculating sum of odd natural numbers upto 'n' Using recurrsion
def sum_odd_numbers(n):
    if n <= 0:
        return 0
    elif (n%2==0):
        return((n-1) +sum_odd_numbers(n-3)) 
    else:
        return(n+sum_odd_numbers(n-1))

print("sum of odd natural numbers upto 10 Using recurrsion is: " f"{sum_odd_numbers(10)}")

# calculating sum of odd natural numbers upto 'n' Using iteration
def ittr_sum_odd_numbers(n):
    if n%2==0:
            n -= 1
    result = 0
    while n >=0:
        result += n
        n -= 2
    return(result)
        
print("sum of odd natural numbers upto 10 Using iteration is: " f"{ittr_sum_odd_numbers(10)}")

# Make it general if negative number then probable responce also consider response to string entered