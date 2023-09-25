def isArrayInSortedOrder(A):
    if len(A) == 1 :
        return True
    return A[0] <= A[1] and isArrayInSortedOrder(A[1:])
A = [127, 200, 246, 333, 321, 454, 533, 565, 933]
print(isArrayInSortedOrder(A))