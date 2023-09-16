letter_template = """\t\tThis program by radha is completed on 28-04-2023, 
                    program\'s uploading date is fixed by radha on 28-04-2023,
                    even though it may simply seem a daily routine, but.....
                    It is what it is, It is actually a daily routine of future """
operation = input("Enter the new operation: ")
name = input("Enter new  coder name: ")
date = input("Enter the uploading date: ")
action = input("Enter an approprtiate action")
print((((letter_template.replace('radha',name)).replace('28-04-2023',date)).replace('program',operation)).replace('daily routine',action))