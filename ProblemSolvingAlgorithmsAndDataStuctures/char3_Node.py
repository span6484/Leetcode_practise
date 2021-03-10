class Node:
    def __init__(self, init_data):
        self.head = None  
        self.data = init_data
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
    
    def setNext(self, newnext):
        self.next = newnext

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp