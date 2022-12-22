import sys
class Sqaure:
    '''Class to Claculate and Display Square Area and Perimeter'''
    def __init__(self, s_l):
        '''__init__ Method for assignment of side length for Square
           using try and except'''
        try :
            if type(s_l)== int: # Type error thought at this line which was wrong
                if s_l >= 0:
                     self.side_length = s_l
                else:
                     sys.exit("Square side length cannot be less than 0")
            else:
               raise AttributeError("Side Length of Square should be a possitiveinteger")
        except AttributeError:
            sys.exit("Side of Square should be an integer value")
# need to throw exception here itself to avoid the entry of a negative integer or a string as side length 

    def area_of_square(self):
        '''Method to Calculate and Print the Area for a Square or Return Area(if required)'''
        area = self.side_length**2
        print(f"The Area of Square is {area}")
                 
        # return(area)

    def perimeter_of_square(self):
        '''Method to Calculate and Print the Perimeter for a Square or Return Perimeter (if required)'''
        perimeter = 4*(self.side_length)
        print(f"The Perimeter of Square is {perimeter}")
        # return(perimeter)

class Rectangle:
    '''Class to Claculate and Display Rectangle Area and Perimeter'''
    def __init__(self,length,width):
        '''Method for assignment of length and With of Rectangle'''
# Chek for a possitive length and width using nested if-else block
        if type(length) == int and type(width) == int:
                if (length>=0 and width>=0):
                    self.rectangle_length = length
                    self.rectangle_width = width
                else:
                    sys.exit("Error in Dimensions of the Rectangle")
        else:
            raise AttributeError("Sides of Rectangle should have been an integer value")
        
    def area_of_rectangle(self):
        '''Method to Calculate and Print the Area for a Rectangle or Return Area(if required)'''
        area = self.rectangle_length*self.rectangle_width
        print(f"The Area of Rectangle is {area}")
        # return(area)

    def perimeter_of_rectangle(self):
        '''Method to Calculate and Print the Perimeter for a Rectangle or Return Perimeter (if required)'''
        perimeter = 2*(self.rectangle_length + self.rectangle_width)
        print(f"The Perimeter of Rectangle is {perimeter}")
        # return(perimeter)

class Circle:
    PI = (22/7)
    '''Class to Claculate and Display Circle Area and Perimeter'''
    def __init__(self, radius):
        '''Method for assignment of radius for Circle'''
        try :
            if(type(radius)== int):
                if radius >= 0:
                   self.circle_radius = radius
            else:
                sys.exit("Negative Radius circle not defined")
        except TypeError:
            sys.exit("Radius should have been an integer value")
        
    def area_of_circle(self):
        '''Method to Calculate and Print the Area for a Circle or Return Area(if required)'''
        area = self.PI*self.circle_radius**2
        print(f"The Area of Circle is {area}")
        # return(area)

    def perimeter_of_circle(self):
        '''Method to Calculate and Print the Perimeter for a Circle or Return Perimeter (if required)'''
        perimeter = 4*self.PI*self.circle_radius
        print(f"The Perimeter of the Circle is {perimeter}")
        # return(perimeter)

print(sys.version)
print(sys.path)

sqaure1 = Sqaure(10)
sqaure1.area_of_square()
sqaure1.perimeter_of_square()

rectangle1 = Rectangle(10,20)
rectangle1.area_of_rectangle()
rectangle1.perimeter_of_rectangle()

circle1 = Circle(15)
circle1.area_of_circle()
circle1.perimeter_of_circle()

rectangle2 = Rectangle(0,0)
rectangle2.area_of_rectangle()
rectangle2.perimeter_of_rectangle()

sqaure2 = Sqaure('y')
sqaure2.area_of_square()
sqaure2.perimeter_of_square()

circle2 = Circle(-10)
circle2.area_of_circle()
circle2.perimeter_of_circle()