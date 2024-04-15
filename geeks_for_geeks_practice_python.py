## Python List Exercises
from typing import List
from operator import length_hint, itemgetter, countOf,contains
from collections import Counter
import pandas as pd
import numpy as np
import re
from statistics import mode

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

#### Approach 6 Using enumrate
def list_index_enumrate(element_list :List, index_list :List) -> List:
    """
    First conert the element list into a {index: element} dictionary 
    using enumrate then use getitem function on the resultant dictionary
    for each element of the index list by get item operator([])
    """
    indexed_dictionary = {index:element for index,element in enumerate(element_list)}
    return list((indexed_dictionary[i] for i in index_list))
assert(list_index_enumrate([1,2,3],[1,2]) == [2,3])
print("Found list elements through Approach 6")

#### 3. Python program to find the String in a List
            ### Solution ###
#### Approach 1 :- Using the 'in' operator
def string_in_list(input_list :List, check_string :str) -> bool: 
    """
    Use 'in' oprator to verify presence of string
    in the list
    """
    return check_string in input_list 
assert(string_in_list([1,'hello',2],'hello') == True)
assert(string_in_list([1,'hello',2],'bye') == False)
print("Checked the occurance of string in the list using approach 1")

#### Approach 2 :- Using count method of the list
def count_string_inlist(input_list :List,test_string :str) -> bool:
    """
    Count the occurance of string if
    it is greater than 1 return True 
    """
    return input_list.count(test_string) > 0
assert(count_string_inlist([1,'hello',2],'hello') == True)
assert(count_string_inlist([1,'hello',2],'bye') == False)
print("Checked the occurance of string in the list using approach 2")

#### Approach 3 :- Using List Comprehension
def lis_comp_for_str_in_list(input_list :List, test_string :str) -> bool:
    """
    return_list contain all occurances of test_string in input_list 
    made by list comprehension if length of return_list > 0 return True
    """
    return_list = [i for i in input_list if test_string in input_list]
    return len(return_list) > 0
assert(lis_comp_for_str_in_list([1,'hello',2],'hello') == True)
assert(lis_comp_for_str_in_list([1,'hello',2],'bye') == False)
print("Checked the occurance of string in the list using approach 3")

#### Approach 4 :- Using any function
def check_str_in_list_any(input_list :List, test_string :str) -> bool:
    """
    Use any function to check if any element in list same as string
    """
    return any(test_string == i for i in input_list)
assert(check_str_in_list_any([1,'hello',2],'hello') == True)
assert(check_str_in_list_any([1,'hello',2],'bye') == False)
print("Checked the occurance of string in the list using approach 4")

#### Approach 5 :- Using map and find function
def map_list_contains_str(input_list :List, test_string :str) -> bool:
    """
    Map the input_list to a list of strings
    use find function on the sring_list which
    returns -1 if test_string not found
    """
    string_list = list(map(str,input_list))
    combined_str = " ".join(string_list)
    return combined_str.find(test_string) != -1
assert(map_list_contains_str([1,'hello',2],'hello') == True)
assert(map_list_contains_str([1,'hello',2],'bye') == False)
print("Checked the occurance of string in the list using approach 5")

#### Approach 6 :- Using countOf method of operator module
def countOf_str_inlist(input_list :List,test_string :str) -> bool:
    """
    Using operator.countOf method ensures list has atleast one count of the string
    """
    return countOf(input_list,test_string) != 0
assert(countOf_str_inlist([1,'hello',2],'hello') == True)
assert(countOf_str_inlist([1,'hello',2],'bye') == False)
print("Checked the occurance of string in the list using approach 6")

#### Approach 7 :- Using contains method of operator module
def list_contains_str(input_list :List, test_string :str) -> bool :
    """
    Uses operator.contains method to check whether list contains string
    """
    return contains(input_list,test_string)
assert(list_contains_str([1,'hello',2],'hello') == True)
assert(list_contains_str([1,'hello',2],'bye') == False)
print("Checked the occurance of string in the list using approach 7")

#### Approach 8 :- Using 're' module 
def str_isinstance_research(input_list :List, test_string :str) -> bool:
    """
    First verify whether a list contains a string or not
    if it contains a string, test_string is matched with
    the contained string using re.search
    """
    result = False
    for item in input_list:
        if (isinstance(item,str)):
            result = bool(re.search(test_string,item))
    return result       

assert(str_isinstance_research([1,'hello',2],'hello') == True)
assert(str_isinstance_research([1,'hello',2],'bye') == False)
print("Checked the occurance of string in the list using approach 8")

#### Approach 9 :- Using ' enumrate ' function
def str_enumrate_research(input_list :List, test_string :str) -> bool:
    """
    First enumrate the list, loop over enumrate object to 
    find an instance of string object if string found compare
    it with the test_string to check the presence
    """
    result = False
    for _,item in enumerate(input_list):
        if (isinstance(item,str)):
            result= bool(re.search(test_string,item))
    return result
assert(str_enumrate_research([1,'hello',2],'hello') == True)
assert(str_enumrate_research([1,'hello',2],'bye') == False)
print("Checked the occurance of string in the list using approach 9")

#### 4. Python Ways to find indices of value in list
            ### Solution ###

#### Approach 1 :- Naive method
def indices_for_value_naive(input_list :List, res_value :int) -> List:
    """
    Start with an empty return_list, Loop through the input_list
    check whether the res_value is equal to list element in case 
    the values are equal append the index value to the return_list
    return the list when loop ends 
    """
    return_list = []
    for i in range(len(input_list)):
        if input_list[i] == res_value:
            return_list.append(i)
    return return_list

assert(indices_for_value_naive([1,3,4,5,6,4,5,6,7,3,4,5],5) == [3,6,11])
print("Found the list indices for the given value by Approach 1")

#### Approach 2 :- Naive method with list comprehenssion 
def value_indices_in_list(input_list :List, res_value :int) -> List:
    """
    Loop over the input_list to find the indicies having the value = res_value
    Construct the return_list containing all indices using list comprehension 
    """
    return_list = [i for i in range(len(input_list)) if input_list[i] == res_value ]
    return return_list
assert(value_indices_in_list([1,3,4,5,6,4,5,6,7,3,4,5],5) == [3,6,11])
print("Found the list indices for the given value by Approach 2")

#### Approach 3 :- Naive method with list comprehenssion along with enumrate
def enum_value_indices_in_list(input_list : List, res_value :int) -> List:
    """
    Use enumrate along with the list comprehension to create the return_list
    """
    return_list = [index for index,value in enumerate(input_list) if value == res_value]
    return return_list
assert(enum_value_indices_in_list([1,3,4,5,6,4,5,6,7,3,4,5],5) == [3,6,11])
print("Found the list indices for the given value by Approach 3")

#### Approach 4 :- Using the filter method
def filter_value_insides_in_list(input_list :List,res_value :int) -> List:
    """
    Creates return_list using list comprehension using and lambda function 
    to filter out the list indices having the value equal to res_value 
    """
    return_list = [i for i in filter(lambda x:input_list[x] == res_value,range(len(input_list)))]
    return return_list
assert(filter_value_insides_in_list([1,3,4,5,6,4,5,6,7,3,4,5],5) == [3,6,11])
print("Found the list indices for the given value by Approach 4")

#### Approach 5 :- Using the numpy library
def numpy_tofind_index_inlist(input_list :List,res_value :int) -> List:
    """
    The numpy array is used to know the indices where the list has a
    value equal to the res_value
    """
    test_array = np.array(input_list)
    return_list = np.where(test_array == res_value)[0]
    return list(return_list)
assert(numpy_tofind_index_inlist([1,3,4,5,6,4,5,6,7,3,4,5],5) == [3,6,11])
print("Found the list indices for the given value by Approach 5")

#### 5. Python Find most frequent element in a list
            ### Solution ###

#### Approach 1 :- Naive Approach
def most_frequent_in_list(input_list :List) -> int:
    """
    Loop over the entire list to count occurance of every element
    For the element having highest occurance return number 
    """
    occurance = 0
    num = input_list[0]
    for i in input_list:
        current_occurance = input_list.count(i)
        if (current_occurance > occurance):
            occurance = current_occurance
            num = i
    return num
assert(most_frequent_in_list([1,3,5,6,4,5,6,7,3,4,5]) == 5)
print("Found most common element of list using Approach 1")

#### Approach 2 :- Pythonic Naive Approach
def most_frequent_of_list(input_list :List) -> int:
    """
    Make the set of element eliminating duplicates
    return the element of set having maximum count in list
    """
    return max(set(input_list),key=input_list.count)
assert(most_frequent_of_list([1,3,5,6,4,5,6,7,3,4,5]) == 5)
print("Found most common element of list using Approach 2")

#### Approach 3 :- Using counter return the most_common element
def most_frequent_using_counter(input_list :List) -> int:
    """
    Create the counter object out of list return
    the most_common element of counter object
    """
    counter_list = Counter(input_list)
    return counter_list.most_common(1)[0][0]
assert(most_frequent_using_counter([1,3,5,6,4,5,6,7,3,4,5]) == 5)
print("Found most common element of list using Approach 3")

#### Approach 4 :- Using the mode of element in List
def most_frequent_with_mode(input_list :List) -> int:
    """
    Uses mode to return the most commonly 
    occuring element of the list
    """
    return mode(input_list)
assert(most_frequent_with_mode([1,3,5,6,4,5,6,7,3,4,5]) == 5)
print("Found most common element of list using Approach 4")

#### Approach 5 :- Using the python dictionary
def most_frequent_with_pyton_dict(input_list :List) -> int:
    """
    Using python dictionary to store list element as key
    and the occurance of element as its value
    """
    dict = {}
    max_count, element = 0, ''
    for item in input_list:
        dict[item] = dict.get(item,0)+1
        if dict[item] >= max_count:
            max_count,itm = dict[item],item
    return itm
assert(most_frequent_with_pyton_dict([1,3,5,6,4,5,6,7,3,4,5]) == 5)
print("Found most common element of list using Approach 5")

#### Approach 6 :- Using the pandas library
def most_frequent_item_list_using_pandas(input_list :List) -> List:
    """
    Create a Data Frame using the inout_list further create a new
    data frame using the value_counts() returns the count based on
    the grouped column values 
    """
    df = pd.DataFrame({'Number':List})