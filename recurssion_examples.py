# def Print(n):
#     if n == 0: return 0
#     else:
#         print (n)
#         return Print(n-1)
# print(Print(6))


# def TowerofHanoi(numberofDisk,StartPeg = 1, EndPeg = 3):
#     if numberofDisk:
#         TowerofHanoi(numberofDisk-1,StartPeg,6-StartPeg-EndPeg)
#         print("Move Disk %d from peg %d to peg %d " % (numberofDisk,StartPeg,EndPeg))
#         TowerofHanoi(numberofDisk-1, 6-StartPeg-EndPeg, EndPeg)
# TowerofHanoi(numberofDisk=4)


def isArratInsortedOrder(A):
    if len(A) == 1:
        return True
    return A[0]<A[1] and isArratInsortedOrder(A[1:])
A = [127,220,246,277,321,454,534,565,933]
print(isArratInsortedOrder(A))