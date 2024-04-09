## Python List Exercises
from typing import List
from operator import length_hint
from collections import Counter
from operator import itemgetter
import numpy as np

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

#### 2. Python Program to Find the length of a List
            ### Solution ###

#### Approach 1 :- Using Naive Method
def naive_list_length(input_list :List) -> int:
    """
    Initial value counter is set to 0,
    increase the counter by 1 while 
    itterating through list"""
    counter = 0
    for i in input_list:
        counter+=1
    return counter
assert(naive_list_length([2,3,4,5,6,7]) == 6)
print("Found List length using Approach 1")

#### Approach 2 :- Using operator.length_hint() method.
def list_length_using_operator(input_list :List) -> int:
    """
    Calculate the using a lesser known function 
    of operator module i.e. length_hint
    """
    return length_hint(input_list)
assert(list_length_using_operator([2,3,4,5,6,7]) == 6)
print("Found List length using Approach 2")

#### Approach 3 :- Using sum() Function with list comprehension
def list_length_with_sum(input_list : List) -> int:
    """
    Using List comprehension genrate 1 for every element and 
    sum them to find list length 
    """
    return sum(1 for i in input_list)
assert(list_length_with_sum([2,3,4,5,6,7]) == 6)
print("Found List length using Approach 3")

#### Approach 4 :- Using sum() function along with counter
def list_length_with_counter(input_list :List) -> int:
    """ 
    Generates the element dictionary with key as element and
    occurance of element as it's count and returns the sum of
    values as list length
    """
    list_element_dict =  Counter(input_list)
    return sum(list_element_dict.values)
assert(list_length_with_sum([2,3,4,5,6,7]) == 6)
print("Found List length using Approach 4")

#### Approach 5 :- Using recurrsion
def list_length_by_recurssion(input_list :List) -> int:
    """
    Make a recursion call to function for the input_list without first element
    add 1 to recurssion call further return 0 for an empty list
    """
    if not input_list:
        return 0 
    return 1+list_length_by_recurssion(input_list[1:])
assert(list_length_by_recurssion([2,3,4,5,6,7]) == 6)
print("Found List length using Approach 5")

#### 3. Find elements of a list by indices
#### Description:- Given two lists with elements and indices,
#### write a Python program to find elements of list 1 at indices present in list 2. 
            ### Solution ###
#### Approach -1 Naive method
def find_list_element(element_list :List, index_list :List) -> List:
    """ 
    Start with an empty list Loop over index_list and append elements
    of element_list present at every each index into return_list
    """
    assert max(index_list) <= len(element_list)-1,"elements of index list cannot greater than equal length of element list"
    return_list = []
    for i in index_list:
        return_list.append(element_list[i])
    return return_list

assert(find_list_element([1,2,3],[1,2]) == [2,3])
print("Found list elements through Approach 1")

#### Approach -2 Naive method with list comprehension

def find_list_element_using_comprehension(element_list :List, index_list :List) -> List:
    """ 
    Returns the desired list through list comprehension 
    """
    assert max(index_list) <= len(element_list)-1,"elements of index list cannot greater than equal length of element list"
    return [element_list[i] for i in index_list]

assert(find_list_element_using_comprehension([1,2,3],[1,2]) == [2,3])
print("Found list elements through Approach 2")

#### Approach -3 Using Map function

def list_element_using_map(element_list :List, index_list :List) -> List:
    """
    Applies element_list.__getitem__ function on index_list 
    returns a map object, first converted to list then returned 
    """
    return list(map(element_list.__getitem__,index_list))
assert(list_element_using_map([1,2,3],[1,2]) == [2,3])
print("Found list elements through Approach 3")

#### Approach 4 Using operator.itemgetter()
def list_item_getter(element_list :List, index_list :List) -> List:
    """
    Uses item getter function of operator module which operates on two tuples.
    First tuple containing indeces of item to extract from element_list
    followed by element_index from which the element is to be extracted
    the result obtained from the item geeter is a tuple hence converted to list
    """
    return list(itemgetter (*index_list)(element_list))
assert(list_item_getter([1,2,3],[1,2]) == [2,3])
print("Found list elements through Approach 4")

#### Approach 5 Using numpy
def list_of_numpy(element_list :List, index_list :List) -> List:
    """
    First convert the element_list into numpy array then
    use the list of index to retrive the desired elements
    """
    return np.array(element_list)[index_list].tolist()
assert(list_of_numpy([1,2,3],[1,2]) == [2,3])
print("Found list elements through Approach 5")

