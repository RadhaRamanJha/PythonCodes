from sll_node import Node
class Linked_List():
    def __init__(self):
        self.head = None
    # to calculate list length 
    def list_length(self):
        current = self.head
        count = 0 
        while current != None:
            count += 1
            current = current.getNext()
    