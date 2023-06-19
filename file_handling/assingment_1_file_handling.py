 # Creation of '.txt' file using "write()"
s = "This is my first program of file handling"
file = open("normla.txt", "w")
file.write(s)
print("\t\tFile Created")
file.close()

# Use of  file handling method "read()" a file 
file2 = open("normla.txt","r")
print("\n\t\tFile Read now Printing it")
print(file2.read())
file2.close()

# Read an existing file using it's location
file4=open(r"C:\Users\radha\OneDrive\Desktop\demo.txt","r")
print("\n\t File Read now Printing it")
print(file4.read())
file4.close()

