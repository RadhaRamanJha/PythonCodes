class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Linked_list():
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data,self.head)
        self.head = node
    
    def Print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ' '
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        
        print(llstr)

if __name__ == "__main__":
    ll = Linked_list()
    ll.insert_at_begining(17)
    ll.insert_at_begining(1)
    ll.insert_at_begining(5)
    ll.Print()
            