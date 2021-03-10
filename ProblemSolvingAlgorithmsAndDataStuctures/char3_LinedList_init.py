import char3_Node

class LinedList:

    def __init__(self):
        self.head = None
        self.end = None
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            
            else:
                previous = current
                current = current.getNext()
        
        if previous == None:
            self.head = current.getNext()
        
        else:
            previous.setNext(current.getNext())



l = LinedList()
l.head = char3_Node.Node(1)
l.head.setNext(char3_Node.Node(2))
l.head.next.next = l.end
print(l.size())
print(l.search(2))
l.remove(2)
print(l.head.data)