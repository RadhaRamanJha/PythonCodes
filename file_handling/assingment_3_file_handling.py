modified_demo = open(r"C:\Users\radha\OneDrive\Desktop\demo.txt","a+")
modified_demo.write("\n\t\tThis is an addition to the demo file")
modified_demo.write("\n\t\tI will try to print each line in next go")
modified_demo.seek(0) # Most important part of this program as this line  
# bring the control at begining of the file so that operations to be done in next lines 
# ca n be done to the ebtire file
content = modified_demo.readlines()
print(content) 
modified_demo.close()
