# A Python program to demonstrate inheritance

class Work_men():
    # Constructor of the employee class
    def __init__(self,worker_name,worker_id):
        self.name = worker_name
        self.id = worker_id
    # Founticion to extract information of employee
    def worker_information(self):
        print(f"{self.name} is the new joinee. The ID number for {self.name} is {self.id}")

lab_assistant = Work_men("Deepak", 1346)
lab_assistant.worker_information()

class Mason(Work_men):

    def