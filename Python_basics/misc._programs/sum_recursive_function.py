import re

def recur_addition(n):
    if n==0:
        return 0
    else:
        return (n + recur_addition(n-1))
print(f"The Tail Recurrcive addition from 10 to 0 is {recur_addition(10)}")