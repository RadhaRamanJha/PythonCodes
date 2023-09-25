#fibbonaci series upto 100th  item
def fibbo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return(fibbo(n-1)+fibbo(n-2))
fibbo_sequence = [fibbo(n) for n in range(10)]
print(fibbo_sequence) # first 10 terms using recursion

# next 90 using concept of fibonaci series
current_number = fibbo(10)
previous_number = fibbo(9)
for n in range(10,101):
    Calculated_fibbo_numbers = []
    next_number = current_number + previous_number
    fibbo_sequence.append(next_number)
    previous_number = current_number
    current_number = next_number
print(fibbo_sequence)