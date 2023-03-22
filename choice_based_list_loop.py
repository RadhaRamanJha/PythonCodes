even_list = []
odd_list = []
entered_sequence = []
class list_operations:
    # filling list 
    def list_filling(self):
        number = int(input("Enter a number for filling list: "))
        if (number % 2 == 0):
            self.list_append(even_list,number)
        elif (number % 2 != 0):
            self.list_append(odd_list,number)
        self.continue_query()
    
    # Query for continuing list filling
    def continue_query(self):
        continue_query = input("Do you want to enter another number (y/n)")
        if continue_query == 'y':
            self.list_filling()
        else:
            self.user_choice_entry()
    
    # List appending operation
    def list_append(self,concrened_list, current_number):
        concrened_list.append(current_number)
        entered_sequence.append(current_number)

    # Obtain last entered even number
    def even_number_popping(self):
        print("The last entered even number is :- ")
        self.number_popping(even_list)
        self.user_choice_entry()

    # Obtain last entered odd number
    def odd_number_popping(self):
        print("The last entered odd number is :- ")
        self.number_popping(odd_list)
        self.user_choice_entry()

    # pop the list and return last entered number    
    def number_popping(self,concerned_list):
        if (len(concerned_list) != 0):
            poped_number = concerned_list.pop()
            print(poped_number)
            if poped_number in entered_sequence:
                entered_sequence.remove(poped_number)
        else:
            print("No numbers left in updated list to Display")
            exit()
    
    # Display sequence of last number entery
    def entered_sequence_display(self):
        if (len(entered_sequence) != 0):
            last_entered_number = entered_sequence[-1]
            print(f"The entered number is {last_entered_number}")
            entered_sequence.remove(last_entered_number)
        else:
            print("All the sequence of entered number has been displayed")
        self.user_choice_entry()

    # Obtaining user choice which fountion to execute
    def user_choice_entry(self):
        self.choices_display()
        while True:
            if (self.choice == 0):
                break
            elif (self.choice == 1):
                self.list_filling()
            elif (self.choice == 2):
                self.even_number_popping()        
            elif (self.choice == 3):
                self.odd_number_popping()
            elif (self.choice == 4):
                self.entered_sequence_display()
            else:
                print("Please Choose among the choice provied")
        
    # Choice presenter
    def choices_display(self):
        print("\tpress 0 anytime to quit\n")
        print("""
             Press 1 to enter a number
             Press 2 to pop and know last even number
             Press 3 to pop and know last odd number
             Press 4 determine the entered sequence of nummbers
             """)    
        self.choice = int(input("Enter your choice among (1/2/3/4) to continue: "))

llo = list_operations()
llo.user_choice_entry()