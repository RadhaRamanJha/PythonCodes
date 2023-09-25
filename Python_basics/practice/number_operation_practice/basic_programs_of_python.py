"""Basic Python Programs excercises from geeksForgeeks 'https://www.geeksforgeeks.org/python-programming-examples/'"""
class basic_programs():
    def __init__(self):
         pass
    def numbers_sum(self,number1,number2):
        """Return sum of two nummbers"""
        if ((type(number1) == int or type(number1) ==  float) and
             (type(number2) == int or type(number2) == float)):
                sum = number1 + number2
                return(sum)
        else:
            raise Exception("Missing appropriate numbers type")
    
    def max_number(self,number1,number2):
        """Calculation of maximum of two numbers"""
        if ((type(number1) == int or type(number1) ==  float) and
             (type(number2) == int or type(number2) == float)): 
                maximum_number = max(number1,number2)
                return(maximum_number)
        else:
            raise Exception("Missing appropriate numbers type")

    def factorial(self,number):
        """Calculation of factorial for a number"""
        if type(number) == int :
            if number > 1:
                factorial = number*self.factorial(number-1)
                return(factorial)
            elif (number == 0 or number == 1):
                return(1)
            elif (number <0):
                raise Exception("Factorial not defined for negative numbers")           
        else:
            raise TypeError("Missing appropriate data type")
    
    def simple_interest_calculation(self,principal_amount,rate,time):
        """Calculation of Simple intrest"""
        if ((type(principal_amount) == int) or (type(principal_amount) == float) and
            (type(time) == int) or (type(time) == float) and 
            (type(rate) == float or type(rate) == int)):
                simple_intrest = principal_amount*rate*time/100
                return(simple_intrest)
        else:
            raise Exception("Missing appropriate data type")

    def compound_intrest_calculation(self,principal_amount,rate,time):
        """Calculation of compound interest"""
        if (type(principal_amount) == int) or (type(principal_amount) == float):
            if(type(time) == int) or (type(time) == float):
               if(type(rate) == float or type(rate) == int): 
                    future_sum = principal_amount*(1+rate/100)**time
                    compound_interest = future_sum - principal_amount
                    return(compound_interest)
               else:
                   raise Exception("Missing appropriate rate data type")
            else:
                raise Exception("Missing appropriate time data type")
        else:
            raise Exception("Missing appropriate principal data type")
      
    def is_armstrong(self,number):
        """Check for a number being Armstrong number """
        if (type(number)==int):
            power= len(str(number))
            sum = 0
            current_number = number
            for pow in range(1,power+1):
                digit = current_number%10
                sum += digit**power
                current_number = ((current_number-digit)//10)
            if (number == sum):
                return True
            else:
                return False
        else:
            raise Exception("Missing appropriate number type")
 
    def find_circle_area(self,radius_of_circle):
        """Program to find area of a circle"""
        if ((type(radius_of_circle) == int) 
            or (type(radius_of_circle) == float)):
            if (radius_of_circle >= 0):
                Area = 3.14*(radius_of_circle**2)
                return Area
            elif (radius_of_circle < 0):
                raise ValueError("Not Defined")
        else:
            raise Exception("Missing appropriate radius type")
    
    def is_number_prime(self,number):
        """checking wheter entered number is prime or not"""
        if ((type(number)== int)):
            if number >= 2:
                for factor in range (2,number):
                    if number % factor == 0:
                        return False
                return True
            else:
                return False
        else:
            raise Exception("Missing appropriate numbers type")
    
    def return_prime_numbers_in(self,number1,number2):
        """Return all prime numbers in a given range"""
        prime_numbers_in_range = []
        if type(number1)==int and type(number2)==int:
            for number in range(min(number1,number2),max(number1,number2)+1):
                if (self.is_number_prime(number) == True):
                    prime_numbers_in_range.append(number)
            return prime_numbers_in_range
        else:
            raise Exception("Missing appropriate numbers type")
            
    def fibbonaci_number(self,n):
        """Returns the nth fibbonaci_number"""
        a,b = 0,1
        i = 0
        if (type(n) == int): 
            if (n>0):
                while (i < n):
                    fibbonaci_number = a
                    a,b = b,a+b
                    i+=1
                return fibbonaci_number
            else:
                raise ValueError("Series not applicable for negative input")
        else:
            raise Exception("Missing appropriate data type type")
    
    def is_fibbonaci_number(self,number):
        """Checks wheter a number fibbonaci_or_not by eqauting
           current fibbonaci number to the argument number provided"""
        if type(number)==int:
            if (number >=0): 
                a,b = 0,1
                fibbonaci_number = a
                while (fibbonaci_number <= number):
                    if (fibbonaci_number == number):
                        return True
                    fibbonaci_number = b
                    a,b = b,a+b
                return False
            else:
                raise ValueError('Missing appropriate value of \'number\'')
        else:
            raise Exception("Missing appropriate number type")
       
    def position_in_fibbonaci_series(self,n,k):
        """Returns position of kth multiple of 'n' in fibbonaci-series"""
        if(type(n)==int):
            if(type(k)==int):
                a,b,position = 0,1,1
                current_fibbonaci_number = a
                current_k_value = 0
                while (current_k_value <= k):
                    current_fibbonaci_number = b
                    a,b = b,a+b
                    position +=1
                    if (current_fibbonaci_number % n == 0):
                        current_k_value += 1
                        if(current_k_value == k):
                            return position                   
            else:
                raise(TypeError('Missing appropriate position type'))
        else:
            raise Exception("Missing appropriate number type")
   
    def square_sum_of_n_natural_numbers(self,n):
        """Calculates sum of sqares of first 'n' natural numbers"""
        if type(n) == int:
            if n > 0:
                natural_number,sum = 1,1
                for natural_number in range (2,n+1):
                    square = natural_number**2
                    sum += square
            elif (n == 0):
                sum = 0
            elif (n < 0):
                raise ValueError("Negative numbers are not considered as natural numbers")
            return(sum)
        else:
           raise Exception("Missing appropriate number type") 
       
    def cube_sum_of_n_natural_numbers(self,n):
        """Calculates sum of cubes of first 'n' natural numbers"""
        if type(n)==int:
            if n > 0:
                natural_number,sum = 1,1
                for natural_number in range (2,n+1):
                    cube = natural_number**3
                    sum += cube
                return(sum)
            elif n == 0:
                sum = 0
                return sum
            elif n < 0:
                raise ValueError("Negative numbers are not considered as natural numbers")
        else:
            raise Exception("Missing appropriate number type")            