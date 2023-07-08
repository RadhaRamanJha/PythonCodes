"""List exersises given on geeks for geeks 
https://www.geeksforgeeks.org/python-programming-examples/#list """
class List_programs():
    
    def __init__(self):
        """1.Takes comma seperated input from user,
        using split inside a for loop appends element
        in 'self.new_list' using try and except to skip
        any unexpexted values"""
        self.new_list = []
        entered_list = input("Enter a list of numbers seperated by commas(,): ")
        for number in entered_list.split(','):
            """Using this constructor automatically removes empty list
             or tuple (if any) from the list"""
            try:
                list_element = int(number)
                self.new_list.append(list_element)
            except:
                ValueError(print(f"skipping the non int value {number}"))
   
    def swap_first_last(self):
        """2.first last element swapped using temp_var"""
        print(f" Orignal list is: {self.new_list}")
        try:
            if (len(self.new_list) >=2):
                temp_var, self.new_list[-1]= self.new_list[-1], self.new_list[0]
                self.new_list[0] = temp_var
                return self.new_list
            elif (len(self.new_list) == 1):
                return(self.new_list)
        except:
            ValueError(print("Number of list elements not enough to perform the operation"))
          
    def swap_two_elements(self,pos1,pos2):
        """3.Swapped arbitrary elements 
        after first conforming the length of list 
        appropriate for the swap and confirming the 
        value of the two positions enterd is integer 
        of list using multiple assignment and temp_var"""
        print(f" Orignal list is: {self.new_list}")
        if (len(self.new_list) >= 2):
            try:
                if (len(self.new_list)>= max(pos1,pos2)):
                    temp_var,self.new_list[pos1-1] = self.new_list[pos1-1],self.new_list[pos2-1]
                    self.new_list[pos2-1] = temp_var
                    return self.new_list
            except:
                TypeError(print("Positions of list elements to be swapped must be integers"))
    
    def length_of_list(self):
        """4.Calculation of list length using for loop"""
        element_number = 0
        for number in self.new_list:
            element_number += 1
        return(element_number)
    
    def is_element_in_list(self,element):
        """5.Verifies element existance in list using 'in' operator"""
        if (len(self.new_list) >= 1):
            if (element in self.new_list):
                return True
            else:
                return False
        else:
            return 0
    
    def sum_of_list(self):
        """6.Restuns sum of list using a for loop"""
        sum = 0 
        if (len(self.new_list) >= 1):
            for num in self.new_list :
                sum += num
        return(sum)

    def product_of_list(self):
        """7.Returns product of list using a for loop"""
        product = 0
        if (len(self.new_list) >= 1):
            product = 1
            for num in self.new_list :
                product *= num
        return(product)
    
    def smallest_num_list(self):
        """8.Returns smallest num in list"""
        if (len(self.new_list) != 0):
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
            if (number > 0) and (number % 2 == 0):
                even_list.append(number)
        if len(even_list) :
            return(even_list)
        else:
            return("No even number present in given list")

    def odd_in_list(self):
        """13. Used list comprehension to genterate
        odd list and finally returns it"""
        odd_list = [number for number in self.new_list if number >0 if number%2 != 0 ]
        return(odd_list)
    
    def odd_even_in_range(self,start,end):
        """14. Program prints all odd and even
        nummbers in list in a given range"""
        even_num_list = []
        odd_num_list = []
        for number in self.new_list:
            if ((number > start) and (number < end)):
                if (number%2 == 0):
                    even_num_list.append(number)
                if (number%2 != 0):
                    odd_num_list.append(number)
        return(f"Even numbers between 1-100 in list {even_num_list} \n Odd numbers between 1-100 in list {odd_num_list}")
    
    def poss_and_neg_num_in_list(self):
        """15.Returns possitive and negative num in list"""
        poss_list, neg_list = [], []
        for num in self.new_list :
            if num > 0:
                poss_list.append(num)
            if num < 0:
                neg_list.append(num)
        return(f"Possitive numbers of list are {poss_list} \n Negative numbers of list are {neg_list}")
    
    def poss_neg_in_given_range(self,start,end):
        """16.Returns possitive and negative numbers in given range inside list"""
        poss_list, neg_list = [], []
        for num in range(start,end+1):
            if num in self.new_list :
                if num < 0 :
                    neg_list.append(num)
                if num > 0:
                    poss_list.append(num)
        return(f"Possitive numbers in range are {poss_list} \n Negative numbers in range are {neg_list}")
           
    def list_reveresed(self):
        """17.beign with an empty temp_list
        make a copy of orignal list then use
        for loop to pop elements from end of copy 
        and append them to temp_list list finally 
        return the temp_list there by automatically reversing it"""
        element_number = len(self.new_list)
        new_list_copy = self.new_list[:]
        temp_list = []
        for i in range(element_number-1,-1,-1):
            poped_item = new_list_copy.pop(i)
            temp_list.append(poped_item)
        return(temp_list)
    def count_ele_in_list(self,element):
        """18.Count the occurances of given element in list"""
        count = 0
        for num in self.new_list:
            if num == element:
                count+= 1
        return count
    
    def clear_list(self):
        """19.Clears the list by poping each element individually"""
        for i in range(0,len(self.new_list)):
            self.new_list.pop()
        return(self.new_list)
    
    def dup_from_list(self):
        """20. Returns the list of duplicate elements in the list"""
        output_list = []
        for num in self.new_list:
            if (self.new_list.count(num) > 1):
                if num not in output_list:
                    output_list.append(num)
        return(output_list)
    
    def cumm_sum_list(self):
        """21. Returns the list of cummlative sum of elements"""
        output_list = []
        sum = 0
        for num in self.new_list:
            sum += num
            output_list.append(sum)
        return(output_list)
    


lp = List_programs()
print(lp.swap_first_last())
print(lp.swap_two_elements(1,2))
print(lp.length_of_list())