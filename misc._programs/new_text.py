# Reding out one line from each .txt file on my PC 
# and generating another .txt file with name file4
# use_of_readlines(file1,file2,file3)
def use_of_readlines(filea,fileb,filec):
    a = filea.readlines()
    b = fileb.readlines()
    c = filec.readlines()
    files = [a,b,c]
    file4 = open("new.txt","w+")
    for i in range(3):
        for file in files:
            if file[i]:
                file4.write(str(file[i]))
            print("\n a line of one of the files printed\n")
        print(f"\n inreament in {i} Checkpoint")
    print("Done")
# Method 2 - using While loop and EOF property to do the same thing

def use_of_while(fileI, fileJ, fileK):
    file5 = open("file5.txt","w")
    lineOfFile1 = fileI.readline() 
    lineoffile2 = fileJ.readline()
    lineoffile3 = fileK.readline()
    while True: #lineOfFile1 or lineoffile2 or lineoffile3:        
        if lineOfFile1 :
            file5.write(lineOfFile1) 
            lineOfFile1 = fileI.readline()
            print(f"A line of first file added")
        if lineoffile2:
            file5.write(lineoffile2)
            lineoffile2 = fileJ.readline()
            print(f"A line of second file added")
        if lineoffile3:    
            file5.write(lineoffile3)
            lineoffile3 = fileK.readline()
            print(f"A line of third file added")
        if not lineOfFile1 and not lineoffile2 and not lineoffile3:  
            print("End of all three files")
            break
file3 = open(r"C:\Users\radha\OneDrive\Desktop\Python codes\skills_required.txt","r")
file2 = open(r"C:\Users\radha\OneDrive\Desktop\Python codes\intro.txt","r")
file1 = open(r"C:\Users\radha\OneDrive\Desktop\demo.txt","r")
use_of_while(file1,file2,file3)