"""Defention of operations"""
def add(num1,num2):
    print (num1+num2)
def subs(num1,num2):
    print(num1-num2)
def mul(num1,num2):
    print(num1*num2)
def div(num1,num2):
    print(num1/num2)
def pow(num1,num2):
    print(num1**num2)
def flor_div(num1,num2):
    print(num1//num2)
def opr_recog(user_entry):
    operations = ['**','//','+','-','*','/']
    for operation in operations:
        if operation in user_entry:
            pres_oper = operation
            return(pres_oper)

"""Obtaining numbers and operations from user"""
user_entry = input("Enter two numbers seperated by desired operation: ")
pres_opr = opr_recog(user_entry)
num_oper_index = user_entry.find(pres_opr)
number1 = int(user_entry[:num_oper_index])
number2 = int(user_entry[num_oper_index+len(pres_opr):])

if ("**" in user_entry):
    pow(number1,number2)
elif ("//" in user_entry):
    flor_div(number1,number2)
elif ("+" in user_entry):
    add(number1,number2)
elif ("-" in user_entry):
    subs(number1,number2)
elif ("*" in user_entry):
    mul(number1,number2)
elif ("/" in user_entry):
    div(number1,number2)
