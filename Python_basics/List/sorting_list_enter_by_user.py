# Arranging the given list in increasing order 
# Method 1 - Finding the size of list 
#            and swapping the first and last elements
#            by using their index    
def swap_list(new_list):
    size = len(new_list)
    new_list[0],new_list[size-1] = new_list[size-1],new_list[0]
    return(print(new_list))
new_list = [9,1,2,3,4,5,6,7,8,0]
swap_list(new_list)
# Method 2 - Swapping first and last digit directly
#            since index of second element is 1 and last element is -1
def swap_list(new_list):
    new_list[0],new_list[-1] = new_list[-1],new_list[0]
    return(print(new_list))
new_list = [0,9,2,3,4,5,6,7,8,1]