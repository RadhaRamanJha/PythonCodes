"""clear list program not done yet will do it in last"""
"""List exersises given on geeks for geeks 
https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/ """
class List_programs():
    
    def __init__(self):
        """1.Takes comma seperated input from user,
        using split inside a for loop appends element
        in 'self.new_list' using try and except to skip
        any unexpexted values"""
        self.new_list = []
        entered_list = input("Enter a list of numbers seperated by commas(,): ")
        for number in entered_list.split(','):
            try:
                list_element = int(number)
                self.new_list.append(list_element)
            except:
                ValueError(print(f"skipping the non int value {number}"))
        print(f" Orignal list is: {self.new_list}")
    
    def swap_first_last(self):
        """2.first last element swapped using temp_var"""
        print("Swapping 1st and last element retuens")
        if (len(self.new_list) >=2):
            temp_var, self.new_list[-1]= self.new_list[-1], self.new_list[0]
            self.new_list[0] = temp_var
            return self.new_list
        elif (len(self.new_list) == 1):
            return(self.new_list)
        elif (len(self.new_list) == 0):
            raise ValueError("Not sufficient elements in list")
          
    def swap_two_elements(self,pos1,pos2):
        """3.Arbitrary elements of list using
        multiple assignment and temp_var"""
        print("Swapping two element at any arbitrary places")
        temp_var,self.new_list[pos1-1] = self.new_list[pos1-1],self.new_list[pos2-1]
        self.new_list[pos2-1] = temp_var
        return self.new_list
    
    def length_of_list(self):
        """4.Calculation of list length using for loop"""
        print(f"length of {self.new_list} is: ")
        element_number = 0
        for number in self.new_list:
            element_number += 1
        return(element_number)
    
    def is_element_in_list(self,element):
        """5.Verifies element existance in list using 'in' operator"""
        if (element in self.new_list):
            return True
        else:
            return False
    
    def sum_of_list(self):
        """6.Restuns sum of list"""
        sum = 0 
        for num in self.new_list :
            sum += num
        return(sum)
    def product_of_list(self):
        """7.Returns product of list"""
        product = 1
        for num in self.new_list :
            product *= num
        return(product)
    
    def smallest_num_list(self):
        """8.Returns smallest num in list"""
        smallest_num = self.new_list[0]
        for num in self.new_list :
            if num < smallest_num :
                smallest_num = num
        return(smallest_num)
    
    def largest_num_list(self):
        """9.Returns the largest element in the list"""
        largest_num = self.new_list[0]
        for num in self.new_list:
            if num > largest_num :
                largest_num = num
        return(largest_num)
    
    def second_lar_num_list(self):
        """10.Returns the second largest elememt if list"""
        largest_num = self.largest_num_list()
        self.new_list.remove(largest_num)
        result = self.largest_num_list()
        self.new_list.append(largest_num)
        return(result)

    def n_lar_ele_list(self,n):
        """11.Returns the 'n' largest numbers of list"""
        return_list = []
        while n > 0 :
            largest_num = self.largest_num_list()
            return_list.append(largest_num)
            self.new_list.remove(largest_num)
            n-=1
        for num in return_list :
            self.new_list.append(num)
        return(return_list)
    
    def even_in_list(self):
        """12. checks the type of element 
        present and appends it to even list and
        finally returns it"""
        even_list = []
        for number in self.new_list :
            if (number % 2 == 0) :
                even_list.append(number)
        if len(even_list) :
            return(even_list)
        else:
            return("No even number present in given list")

    def odd_in_list(self):
        """13. Used list comprehension to genterate
        odd list and finally returns it"""
        odd_list = [number for number in self.new_list if type(number) == int if number%2 != 0 ]
        return(odd_list)
    
    def list_reveresed(self):
        """14.Pops element from list
        and enter the elemet in temp_list
        in reverse order"""
        element_number = len(self.new_list)
        new_list_copy = self.new_list[:]
        temp_list = []
        for i in range(element_number-1,-1,-1):
            poped_item = new_list_copy.pop(i)
            temp_list.append(poped_item)
        return(temp_list)
   
lp = List_programs()
print(lp.swap_first_last())
print(lp.swap_two_elements(2,3))
print(lp.length_of_list())
print(lp.is_element_in_list(5))
print(lp.sum_of_list())
print(lp.product_of_list())
print(lp.smallest_num_list())
print(lp.largest_num_list())
print(lp.second_lar_num_list())
print(lp.n_lar_ele_list(3))
print(lp.even_in_list())
print(lp.odd_in_list())
print(lp.list_reveresed())