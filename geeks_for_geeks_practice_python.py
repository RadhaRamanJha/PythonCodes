## Python List Exercises
from typing import List

#### 1. Python program to interchange first and last elements in a list
            ### Solution ###

##### Approach 1 :- Find length(l) of list swap the first element and (l-1)th element of the list
def swap_first_and_last(input_list:List)->List:

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

assert(swap_first_and_last([2,3,4])== [4,3,2])

print("Swapped first and Last list element by approach 1")

##### Approach 2 :- since last element of input list can be referred as input_list[-1] we can simply swap input_list[-1] and input_list[0]
def first_last_element_swap_list(input_list: List)->List:

    """After verifying the input type is list interchange
       list elements using comma assignment in a single line"""
    
    if (type(input_list) == list):
        input_list[0],input_list[-1] = input_list[-1],input_list[0]
    else:
        print(f"The function works only for the list the input type provided is {type(input_list)}")

    return(input_list)

assert(first_last_element_swap_list([6,3,8])== [8,3,6])

print("Swapped first and Last list element by approach 2")

##### Approach 3 :- First use the argument operator(*) to unpack list and rearange it
def last_first_swap(input_list:List)->List:

    """ use variables a,*b,c to store the list as tuple and
        return the list after rearrangment"""
    
    if (type(input_list) == list):
        a,*b,c = input_list
        input_list = c,*b,a
    else:
        print(f"The function works only for the list the input type provided is {type(input_list)}")
    return input_list

# assert(last_first_swap([9,4,8])== [8,4,9])
# print("Swapped first and Last list element by approach 3")

##### Approach 4 :- Using inbuilt list menthods namely pop() ,append() and insert()
def swapping_via_inbuilt_methods(input_list :List) -> List:

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

assert(swapping_via_inbuilt_methods([19,4,18])== [18,4,19])
print("Swapped first and Last list element by approach 4")

##### Approach 5 :- Using the slicing to swap elements
def swapping_using_slicing(input_list :List) -> List:
    """Use slicing to rearrange the elements of list"""
    if (type(input_list) == list):
        if (len(input_list) >= 2):
            input_list = input_list[-1:]+input_list[1:-1]+input_list[:1]
    else:
        print(f"The function works only for the list the input type provided is {type(input_list)}")
    return input_list

assert(swapping_using_slicing([19,4,18])== [18,4,19])
print("Swapped first and Last list element by approach 5")

#### 2. Python Program to Swap Two Elements in a List
            ### Solution ###

#### Aproach 1 :- Using comma operator interchange the list element at mentioned position
def interchange_list_element(input_list :List,position1 :int,position2 :int):
    """Interchanges the list element at position 1 and postion 2 
       using comma assignment in a single line"""
    if type(input_list) == list:
        input_list[position1], input_list[position2] = input_list[position2],input_list[position1]
    else:
        print(f"The function works only for the list the input type provided is {type(input_list)}")
    return input_list

assert(interchange_list_element([3,4,56,7],3,2) == [3,4,7,56])
print("Swapped list elements at mentioned location by approach 1")

#### Approach 2 :- Using pop and insert list operators
def list_element_interchange(input_list :List, position1:int, position2:int) ->List:
    """Pops the element from list from position1 and position2 
    Then insert the poped elements at position2 and position1 respectively"""
    if type(input_list) == list:
        position1_popped = input_list.pop(position1)
        position2_popped = input_list.pop(position2-1)
        input_list.insert(position1,position2_popped)
        input_list.insert(position2,position1_popped)
    else:
        print(f"The function works only for the list the input type provided is {type(input_list)}")
    return input_list

assert(list_element_interchange([32,35,36,24,37],1,3) == [32,24,36,35,37])
print("Swapped list elements at mentioned location by approach 2")

#### Approach 3 :- Using a tuple and Indexing operator
def swapping_list_element(input_list :List,position1 :int, position2 :int) -> List:
    """Using indexing operator store the list elements at position1 and postion2 as a tuple
       Then using assigment operator swap the location of both the elements"""
    if type(input_list) == list:
        temp_tup = input_list[position1],input_list[position2]
        input_list[position2],input_list[position1] = temp_tup
    else:
        print(f"The function works only for the list the input type provided is {type(input_list)}")
    return input_list

assert(swapping_list_element([32,35,36,24,37],1,3) == [32,24,36,35,37])
print("Swapped list elements at mentioned location by approach 3")

        

# lis1= [2,3,4,5,6,8]
# print(swapping_using_slicing(lis1))
# lis2 = "a,b,c"
# print(swapping_using_slicing(lis2))


