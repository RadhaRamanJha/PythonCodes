## Python List Exercises

#### 1. Python program to interchange first and last elements in a list
            ### Solution ###

##### Approach 1 :- Find length(l) of list swap the first element and (l-1)th element of the list
def swap_first_and_last(input_list):
    """First verify the type of argument is list
       store the first element of list as 'temp' 
       variable and swap first element with 
       last element and last element with the 'temp' variable"""
    if type(input_list) == list:
        temp = input_list[0]
        l = len(input_list)
        input_list[0] = input_list[l-1]
        input_list[l-1] = temp
    else:
        print(f"The function works only for the list the input type provided is {type(input_list)}")
    return(input_list)

##### Approach 2 :- since last element of input list can be referred as input_list[-1] we can simply swap input_list[-1] and input_list[0]
def first_last_element_swap_list(input_list):
    """After verifying the input type is list interchange
       list elements using comma assignment in a single line"""
    if (type(input_list) == list):
        input_list[0],input_list[-1] = input_list[-1],input_list[0]
    else:
        print(f"The function works only for the list the input type provided is {type(input_list)}")
    return(input_list)

##### Approach 3 :- First use the argument operator(*) to unpack list and rearange it
def last_first_swap(input_list):
    """ use variables a,*b,c to store the list as tuple and
        return the list after rearangment"""
    if (type(input_list) == list):
        a,*b,c = input_list
        input_list = c,*b,a
    else:
        print(f"The function works only for the list the input type provided is {type(input_list)}")
    return input_list

##### Approach 4 :- Using inbuilt list menthods namely pop() ,append() and insert()
def swapping_via_inbuilt_methods(input_list):
    """First pop the first and last element of list
       then insert them at last and first position respectively"""
    if (type(input_list) == list):
        first = input_list.pop(0)
        last = input_list.pop(-1)
        input_list.append(first)
        input_list.insert(0,last)
    else:
        print(f"The function works only for the list the input type provided is {type(input_list)}")
    return input_list

##### Approach 5 :- Using the slicing to swap elements
def swapping_using_slicing(input_list):
    """Use slicing to rearrange the elements of list"""
    if (type(input_list) == list):
        if (len(input_list) >= 2):
            input_list = input_list[-1:]+input_list[1:-1]+input_list[:1]
    else:
        print(f"The function works only for the list the input type provided is {type(input_list)}")
    return input_list

#### 2. Python Program to Swap Two Elements in a List
            ### Solution ###

#### Aproach 1 :- Using comma operator interchange the list element at mentioned position
def interchange_list_element(input_list,position1,position2):
    """Interchanges the list element at position 1 and postion 2 
       using comma assignment in a single line"""
    if type(input_list) == list:
        list_len = len(input_list)
        if -list_len <= 

        

lis1= [2,3,4,5,6,8]
print(swapping_using_slicing(lis1))
lis2 = "a,b,c"
print(swapping_using_slicing(lis2))


