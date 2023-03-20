even_list = []
odd_list = []
entered_sequence = []
class list_operations:
    # filling list 
    def list_filling(self):
        current_number = int(input("Enter a number: "))
        if (current_number % 2 == 0):
            even_list.append(current_number)
            entered_sequence.append(current_number)
            print("The updated even number list is")
            print(even_list)
        elif (current_number % 2 != 0):
            odd_list.append(current_number)
            entered_sequence.append(current_number)
            print("The updated odd number list is")
            print(odd_list)
        continue_query = input("Do you want to enter another number (y/n)")
        if continue_query == 'y':
            self.list_filling()
        else:
            self.user_choice_entry()
    # even number popping
    def even_number_popping(self):
        poped_even_number = even_list.pop()
        print("The last entered even number is :- ")
        print(poped_even_number)
        print("Updated Even number list is: ", end=" ")
        print(even_list)
        self.user_choice_entry()
    # odd number popping
    def odd_number_popping(self):
        poped_odd_number = odd_list.pop()
        print(poped_odd_number)
        print("Updated odd number list is: ", end=" ")
        print(odd_list)
        self.user_choice_entry()
    # entered sequence display getting error in it
    def entered_sequence_display(self):
        last_entered_number = entered_sequence.pop()
        while (last_entered_number == self.even_list) or (last_entered_number == self.odd_list) :
            last_entered_number = entered_sequence.pop()
            break
        print(last_entered_number)
        print("updated sequence of entry is: ",end=" ")
        print(entered_sequence)
        self.user_choice_entry()
    # taking user choice to run fontion (2 times asking enter a number for the first time ???)
    def user_choice_entry(self):
        print("press 0 anytime to quit")
        self.choice = int(input("Enter your choice among (1/2/3/4) to continue: "))
        while True:
            if (self.choice == 0):
                break
            elif (self.choice == 1):
                print("Enter a number: ")
                self.list_filling()
            elif (self.choice == 2):
                self.even_number_popping()        
            elif (self.choice == 3):
                self.odd_number_popping()
            elif (self.choice == 4):
                self.entered_sequence_display()
llo = list_operations()
llo.user_choice_entry()