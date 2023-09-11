class A:
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        A.__init__(self)    
        print("B")
class C(B):
    def __init__(self):
        super().__init__() # Instantiation of Parent class 
        print("C")
class D(C):
    def __init__(self):
        super().__init__()
        print("D")
Dog = D()
