# Method 1 - Reading entire file and printing any line by indexing 
file =open("intro.txt", "r")
content = file.readlines()
print("This is the last line\n")
print(content[5])

# Printing 3rd and 4th line
print("\n\t This is the 3rd and 4th line repectively")
print(content[2])
print(content[3])
file.close()

# Method 2- By using "linecache" package
import linecache
print("\n\t\t\tAnd Here comes my final objective !!!")
specific_line = linecache.getline("intro.txt", 4)
print(specific_line)
file.close()

# Appending "intro.txt" to work practice new method of reading lines
file = open("intro.txt","a+")
file.write("\nAdding more lines to the current file")
file.write("\n In fact Just want to practice 'enumrate' method to read line")
file.write("\n I already had 6 lines orignally now this is the 9 th line..just 1 more")
file.write("\nThis compltes my exresice of reading lins")
file.close() 



# Previously when i was trying to read file before closing it
# I was getting index out of range error 
# The reason for the above issue was because
# the pointer is at last character of the last line in previous case 
# to get the desired result i have to use seek() command

file = open("intro.txt","r")
full_text = file.readlines()
print(full_text[9])  

file.close()

# Converting my file into neatly formated list
with open("intro.txt","r") as file:
    list_file = []
    for line in file :
        list_file.append(line.strip()) ## Dicuss why When Bracket was not provied location was returned 
        # when () after strip was provided correct result obtained
    print(list_file)