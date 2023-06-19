# Writing a Program to read first N=2 lines of a file
# 1. By after creating a file (By using (w+) founction)
s = """I am Radha Raman Jha
    even though i am a Btech and Mtech in civil Engineering
    i am reading python now a days
    as eventually i want to be a Data Scientist
    as the job can give me appropriate path to
    earn more and live life with Dignity"""
file1 = open("intro.txt","w+")
file1.write(s)
print("\t\tchecking exection1")
file1.seek(0) # this is to tell python start from begining
print(file1.readlines(5))
z1= file1.read()  
print("\n\t\tchecking exection2")
print(z1) # since pointer has already reached upto 5 bytes it starts from 6th byte starts printing from 'even....'
file1.close()

# By using (w, r) founction seperatly
file2 = open("intro.txt","r")
z = file2.readlines(-1)

print("\n\t\tchecking exection3")
file2.seek(5)
z2 = file2.read(10)
print("\n\t\t nothing to check just for seperation1")
print(z)
print("\n\t\t to check change in program behaviour ")
print(z2) # Printing 10 characters after 5th position due to addition of Seek(5) at line 24
file2.close()
