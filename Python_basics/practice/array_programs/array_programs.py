"""Array Python Programs excercises from geeksForgeeks https://www.geeksforgeeks.org/python-programming-examples/#array"""
class array_programs:
    """Class to perform various operations on array"""
    def __init__(self, array_of_numbers):
        self.list1 = array_of_numbers
        
    def sum(self):
        """Performs sum of all elements of array"""
        sum = 0
        for number in self.list1:
            sum += number
        return(sum)
    
    def max(self):
        """Finds the maximum among all elements in array"""
        max_of_array = self.list1[0]
        for num in self.list1 :
            if num > max_of_array:
                max_of_array = num
        return(max_of_array)
    
    def array_rotation(self,list2):
        """Exectues left rotation of array by one element"""
        list_to_rotate = list2[:]
        popped_item = list_to_rotate.pop(0)
        list_to_rotate.append(popped_item)
        return list_to_rotate
    
    def array_reversal_algo(self,list3,amount):
        """Executes left rotation of array by given number """
        updated_list = list3[:]
        num = 0
        while num in range (0,amount):
            updated_list = self.array_rotation(updated_list)
            num += 1
        return updated_list
    def find_reminder_array_mul(self):
        """Find the reminder of array multiplication"""
        product_of_array = 1
        for num in self.list1 :
            product_of_array *= num
        return(product_of_array % len(self.list1))
    
    def mono_nature(self):
        """Returns wheter list is monotonic"""
        array = self.list1
        if(array[0] > array[1]): # every next element must be lesser than previous
            for i in range(1,len(array)-1):
                if(array[i] <= array[i+1]):
                    return("Not monotonic")                    
            return("Decreasing monotonically")
        elif(array[0]<array[1]): # every next element must be more than previous
            for i in range(1,len(array)-1):
                if(array[i] >= array[i+1]):
                    return("Not monotonic")                    
            return("Increasing monotonically")
        else:
            return("Not monotonic")
    
    def is_mono_arr(self):
        """modified check for monotonic array -- 
        function being monotonic
        number of increase or decrease must be 
        (length of array -1)"""
        arr = self.list1
        num_inc, num_dec, i = 0,0,0
        while i < (len(arr)-1):
            if (arr[i]>arr[i+1]):
                num_dec +=1
            elif(arr[i]<arr[i+1]):
                num_inc +=1
            elif(arr[i] == arr[i+1]):
                return("Not monotonic")
            if ((num_inc>0) and (num_dec>0)):
                return("Not montonic")
            i +=1
        if (num_dec == len(arr)-1):
            return("Decreasing monotonically")
        elif (num_inc == len(arr)-1):
            return("Increasing monotonically")
                          
array_of_numbers1 = [1,2,2]
array_of_numbers2 = [3,4,5]
array_of_numbers3 = [4,5,6,7]
array_of_numbers4 = [2,3,4,3,6,7,8]

a4 = array_programs(array_of_numbers4)
print(a4.sum())
print(a4.max())
print(a4.array_rotation(array_of_numbers4))
print(a4.array_reversal_algo(array_of_numbers4,4))
print(a4.find_reminder_array_mul())
print(a4.mono_nature())
print(a4.is_mono_arr())