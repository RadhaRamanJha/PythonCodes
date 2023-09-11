file = open(r"C:\Users\radha\OneDrive\Desktop\Python codes\intro.txt","r")
# text = file.readline()
# while True:
#     print(f"Line of file:- {file}")

count = 0
while True:
   line = file.readline()
   print(line)
   count+=1

   if not line: # this line is 
       print(count)
       break

file.close()