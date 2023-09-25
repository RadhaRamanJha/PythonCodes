# Node of a Single Linked list 
class Node:
    #constructor
    def __init__(self):
        self.data = None
        self.next = None
    # method for setting data field of node
    def set_data(self,data):
        self.data = data
    # method for getting data field of the node
    def getData(self):
        return self.data
    # method of setting next field of the node
    def setNext(self,next):
        self.next = next
    # method of getting next field of the node
    def getNext(self):
        return self.next
    # returns True if node points to another node
    def hasNext(self):
        return self.next != None