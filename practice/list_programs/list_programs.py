"""clear list program not done yet will do it in last"""
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
            try:
                list_element = int(number)
                self.new_list.append(list_element)
            except:
                ValueError(print(f"skipping the non int value {number}"))
        print(f" Orignal list is: {self.new_list}")
        if (len(self.new_list) != 0):
            print(f"List obtained after swapping fist and last element is {self.swap_first_last()}")
            print(f"List obtained after swapping second and third element of the list is {self.swap_two_elements(2,3)}")
            print(f"Length of the given list is {self.length_of_list()}")
            print(f"The element 7 is present in list {self.is_element_in_list(7)}")
            print(f"The sum of list is {self.sum_of_list()}")
            print(f"The product of list is {self.product_of_list()}")
            print(f"The smallest number in the list is {self.smallest_num_list()}")
            print(f"The largest number in the list is {self.largest_num_list()}")
            print(f"The second largest element of the list is {self.second_lar_num_list()}")
            print(f"The four largest elements of the list are {self.n_lar_ele_list(4)}")
            print(f"The even numbers in the list are {self.even_in_list()}")
            print(f"The odd numbers in the list are {self.odd_in_list()}")
            print(self.odd_even_in_range(1,100))
            print(self.poss_and_neg_num_in_list())
            print(self.poss_neg_in_given_range(-10,10))
            print(f"List obtained by reversing every element {self.list_reveresed()}")
        else:
            print("List is empty so operations cannot be performed")

    
    def swap_first_last(self):
        """2.first last element swapped using temp_var"""
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
        temp_var,self.new_list[pos1-1] = self.new_list[pos1-1],self.new_list[pos2-1]
        self.new_list[pos2-1] = temp_var
        return self.new_list
    
    def length_of_list(self):
        """4.Calculation of list length using for loop"""
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