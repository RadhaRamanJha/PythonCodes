from pickle import TRUE


file = open("intro.txt","r")
line_in_file = file.readlines()
for index, line in enumerate(line_in_file):
     print(line.strip())
     print(f"value of line at {index} is {line.strip()}")
# Printing only those line/lines with word "Data" in it
     # if "Data" in line:
     #  print(f"value of line at {index} is {line.strip()}")
     # if line.__contains__("Data"):
     #  print(line.strip())