natural_number = [0,1,2,3,4,5,6,7,8,9]
n = len(natural_number)
class coustom_list(number_list):
    def __init__(self,number_list):
        self.number_list = number_list
    def list_sum (number_list):
        i = 0 
        sum_of_list = 0
        while i <= n-1:
            sum_of_list += number_list[i]
            i+=1
        print(f"The Sum of all elements of the list is {sum_of_list}")
        return sum_of_list

def list_avg (number_list):
    sum_of_list = list_sum(number_list)
    print(f"Average of the list is {sum_of_list/n}")

# Dry run :- i = 0, n = 10, s_l[0] = 0, s_o_l = 0+0, i = 1; n_l[1] = 1 , 1<=9, s_o_l = 0 + 1, i = 2;
# 2<=9 n_l[2] = 2, s_o_l = 1+2, i =3 ; 3<=9 n_l[3] = 3, s_o_l = 3+3, i = 4 , 4<=9 n_l[4] = 4, s_o_l = 6+4, i =5
# 5<=9 n_l[5] = 5, s_o_l = 10+5, i =6, 6<==9 n_l[6] = 6, s_o_l = 15+6, i =7, 7<=9 n_l[7] = 7, s_o_l = 21+7, i =8
# 8<=9 n_l[8] = 8, s_o_l = 28+8, i = 9, 9<=9 n_l[9] = 9, s_o_l = 36+9, i =10, 10>9 LOOP STOPS
def min_of_list(list1):
    i = 0
    min_number = list1[i]
    for i in range(1,n):
        if (list1[i]<min_number):
            min_number = list1[i]        
    print(f"The Minimum number of list is {min_number}")

def max_of_list(list1):
    i = 0
    max_number = list1[i]
    for i in range(1,n):
        if (list1[i]>max_number):
            max_number = list1[i]         
    print(f"The Maximum number of list is {max_number}")
# DRy_run i = 0 n = 10, min_numb = 0 i = 4, (4<0)
max_of_list(natural_number)
min_of_list(natural_number)
list_sum(natural_number)
list_avg(natural_number)