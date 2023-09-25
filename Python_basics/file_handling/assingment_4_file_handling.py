# Creation of '.txt' file with the use of 'List'

topics = ["Python","Data Visualization","SQL/NoSQL", "Social Media Mining","Fundamental Statistics","Natural Language Processing/Machine Learning","Microsoft Excel", "High-Level Math","Teamwork", "Communication","Business Savvy"]
skills = open("skills_required.txt","w")
skills.write("To sucessfully make my self a Data Scientist:-")
for topic in topics:
     skills.write("\n")
     skills.write(topic)
     skills.write("\n")
     print(f"\n I have to master {topic}")
skills.close()

# Printing statements from file 

languages = open(r"skills_required.txt","r")
for language in languages:
    if len(language.strip()) != 0 :
         # if "Data Scientist" in language:
         print(language)
    else:
        print(f"Planning to master {language.strip()}")
languages.close()
