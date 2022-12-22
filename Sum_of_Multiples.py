# Sum of Multiples itterative
def sum_of_mul(n,k):
    if(type(n)==type(k)==int):
        i = 0 
        sum = 0
        for i in range(0,n+1,k):
            sum += i
        print(f"The itterative sum of multiples of {k} upto {n} is {sum}")
    else:
        print("Need an integer to perform the operation")


sum_of_mul(20,5)
sum_of_mul("ram","shyam")

# Sum of Multiples recurssive
def recc_sum_of_mul(n,k):
    if(type(n)==type(k)==int):
       if(n<k):
            return 0
       else:
            return((n//k)*k + recc_sum_of_mul(n-k,k))
    else:
        return("Integer required")

print(recc_sum_of_mul(21,5))
print(recc_sum_of_mul("ram","shyam"))