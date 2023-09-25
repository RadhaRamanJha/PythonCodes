def swap1(list1):
    i = 0
    n = len(list1) - 1
    while(i<n-i):
        temp_var = list1[i]
        list1[i] = list1[n-i]
        list1[n-i] = temp_var
        i+=1
    print(f"The state of list after swap {list1}")

list2 = [3,7,8,9,10,11]
swap1(list2)


# Dry run :- i = 4 n =7  4<3 : list1 = [8,7,6,5,4,3,2,1], t_v = 4 
# Dry run  :- i=3 n=7 t_v = 3,3<3,list1 = (8,7,6,4,5,3,2,1)

