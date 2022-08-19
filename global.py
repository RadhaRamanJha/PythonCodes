from ast import Add


a = 10
b = 15
c = 20
d = 25
def add():
    global a
    global b
    global c
    global d
    for a in range (10,13):
        sum = a+b+c+d
        a+=1
        print(a)
        print(sum)
add()
print(a)