class A:
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