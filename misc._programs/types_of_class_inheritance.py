# multiple inheritance
class A():
    pass
class C:
    pass
class B(A,C):
    pass
if issubclass (B,(A,C)):
    print("Class B is subclass of Class A and C")
    if isinstance(B,(A,C)):
        print("Class B is instance of A and C")
    else:
        print("Not an instance")
else:
    print("not a subclass")
    
# multiple level inheritance

# Defining Parent class
class Grandfather():
    def __init__(self,name,age):
        self.person_name = name
        self.person_age = age
        self.profession = "Hari Pooja"
    def description(self):
        print(f"Hello my name is {self.person_name},my age is {self.person_age}")
        print(f"My Profession is {self.profession}")


# Defining Intermediatory class 

class Father(Grandfather):
    def __init__(self, name, age, profession = "Retired"):
        super().__init__(name, age)
        self.profession = profession
    def description(self):
        return super().description()


# Defining Derived Class

class Son(Father):
    def __init__(self, name, age, profession):
        super().__init__(name, age, profession)
    def description(self):
        return super().description()

late_gf = Grandfather("R.K.Jha",100)
late_gf.description()
k_jha = Father("K. Jha", 65)
k_jha.description()
k_m_j = Son("Mukund", 35 , "Sr. Software Developer")
r_r_jha = Son("Mukesh", 33, "Learner")
k_m_j.description()
r_r_jha.description()    

# Sigle Inheritance 
class A:
    pass
class B(A):
    pass
if(issubclass(B,A)):
    print("Class B is Subclass of A")

# Hirarical Inheritence
class faculty:
    def __init__(self, faculty_name, faculty_id, faculty_branch):
        self.name = faculty_name
        self.id = faculty_id
        self.branch = faculty_branch
    def describe_faculty(self):
        print(f"{self.name} is a very good facukty of {self.branch}. His Punching ID is {self.id}")
    