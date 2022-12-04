
def swap(list1):
    """Swaps the elements of the list"""
    i = 0
    n = len(list1) - 1
    while(i<n-1-i):
        temp_var = list1[i]
        list1[i] = list1[n-i]
        list1[n-i] = temp_var
        i+=1
    print(f"The state of list after swap {list1} ")
list2 = [1,2,3,4,5,6,7]
swap(list2)
# Dry run  :- i=3 n=7 t_v = 3,3<3,list1 = (8,7,6,4,5,3,2,1)
# Dry run :- i = 3 n = 6 3<1 : t_v = 3, [7,6,5,4,3,2,1]
def swap1(list1):
    i = 0
    n = len(list1) - 1
    while(i<n-i):
        temp_var = list1[i]
        list1[i] = list1[n-i]
        list1[n-i] = temp_var
        i+=1
    print(f"The state of list after swap {list1}")

list2 = [1,2,3,4,5,6,7]
swap1(list2)


# Dry run :- i = 4 n =7  4<3 : list1 = [8,7,6,5,4,3,2,1], t_v = 4 
# Dry run  :- i=3 n=7 t_v = 3,3<3,list1 = (8,7,6,4,5,3,2,1)

