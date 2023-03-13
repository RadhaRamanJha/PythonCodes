even_list = []
odd_list = []
entered_sequence = []
class list_operations:
    def __init__(self):
        pass

    def list_filling(self):
        self.current_number = int(input("Enter a number: "))
        if (self.current_number % 2 == 0):
            even_list.append(self.current_number)
            entered_sequence.append(self.current_number)
            print("The updated even number list is")
            print(even_list)
        elif (self.current_number % 2 != 0):
            odd_list.append(self.current_number)
            entered_sequence.append(self.current_number)
            print("The updated odd number list is")
            print(odd_list)
        continue_query = input("Do you want to enter another number (y/n)")
        if continue_query == 'y':
            list_operations.list_filling()
        else:
            self.user_choice_entry()
    def even_number_popping(self):
        poped_even_number = even_list.pop()
        print("The last entered even number is :- ")
        print(poped_even_number)
        print("Updated Even number list is: ", end=" ")
        print(even_list)
        self.user_choice_entry()
    def odd_number_popping(self):
        poped_odd_number = odd_list.pop()
        print(poped_odd_number)
        print("Updated odd number list is: ", end=" ")
        print(odd_list)
        self.user_choice_entry()
    def entered_sequence_display(self):
        last_entered_number = entered_sequence.pop()
        while (last_entered_number not in self.even_list) or (last_entered_number not in self.odd_list) :
            last_entered_number = entered_sequence.pop()
        print(last_entered_number)
        print("updated sequence of entry is: ",end=" ")
        print(entered_sequence)
        self.user_choice_entry()
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
list_operations.user_choice_entry()