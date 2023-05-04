class basic_programs():
    """Return sum of two nummbers"""
    def numbers_sum(number1,number2):
        print(f"The sum of two number is {number1+number2}")
    
    """Calculation of maximum of two numbers"""
    def max_number(number1,number2):
        print(f"The maximum nummber among the two is {max(number1,number2)}")

    """Calculation of factorial for a number"""
    def factorial(number):
        if number < 0:
            return("not calculable for negative numbers")
        else:
            if (number == 0 or number == 1):
                return 1
            else:
                return(number*basic_programs.factorial(number-1))
     
    """Calculation of Simple intrest"""
    def simple_interest_calculation(principal_amount,rate,time):
        simple_intrest = principal_amount*rate*time/100
        print(f"The Simple Intrest is {simple_intrest}")

    """Calculation of compound interest"""
    def compound_intrest_calculation(principal_amount,rate,time):
        future_sum = principal_amount*(1+rate/100)**time
        compound_interest = future_sum - principal_amount
        print(f"The compound interest is {compound_interest}")
    
    """Check for a number being Armstrong number """
    def is_armstrong(number):
        power= len(str(number))
        sum = 0
        current_number = number
        for pow in range(1,power+1):
            digit = current_number%10
            sum += digit**power
            current_number = ((current_number-digit)//10)
        if (number == sum):
            print(f"Number {number} is armstrong")
        else:
            print(f"Number {number} is not armstrong")

    """Program to find area of a circle"""
    def find_circle_area(radius_of_circle):
        if ((type(radius_of_circle) == int) 
            or (type(radius_of_circle) == float)):
            if radius_of_circle < 0:
                print("Incorrect input enter a possitive number")
            else:
                Area = 3.14*(radius_of_circle**2)
                print(f"The area of circle is {Area}")

    """checking wheter entered number is prime or not"""
    def is_number_prime(number):
        for factor in range (2,number):
            if number % factor == 0:
                return
        return True
    
    """Return all prime numbers in a given range"""
    def return_prime_numbers_in(number1,number2):
        prime_numbers_in_range = []
        for number in range(number1,number2+1):
            if (basic_programs.is_number_prime(number) == True):
                prime_numbers_in_range.append(number)
        print(f"prime numbers in the range are {prime_numbers_in_range}")
        
    """Returns the n-th fibbonaci_number"""
    def fibbonaci_number(n):
        a,b = 0,1
        i = 0 
        while (i < n):
            fibbonaci_number = a
            a,b = b,a+b
            i+=1
        return fibbonaci_number



        

basic_programs.numbers_sum(467,560)
basic_programs.max_number(75,77)
print(f"The factorial of number is {basic_programs.factorial(-1)}")
basic_programs.simple_interest_calculation(500000,10,8)
basic_programs.compound_intrest_calculation(500000,10,8)
basic_programs.find_circle_area(100)
basic_programs.is_armstrong(1634)
print(f"67 is prime {basic_programs.is_number_prime(67)}")
basic_programs.return_prime_numbers_in(2,234)
print(f"The 11th fibbonaci number is {basic_programs.fibbonaci_number(11)}")