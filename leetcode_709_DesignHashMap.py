class Node:
    def __init__(self, val:int, key):
        self.val = val
        self.key = key
        self.next = None
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """ 
        dummy_key = 100
        dummy_val = 100
        self.length = 1000
        self.array = [Node(dummy_val, dummy_key) for i in range(self.length)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        h_value = hash(key) % self.length
        dummy_head = self.array[h_value]
        cur = dummy_head
        while cur.next != None and cur.next.key != key:
            cur = cur.next
        if cur.next != None:
            cur.next.val = value
        else:
            cur.next = Node(value, key)


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        h_value = hash(key) % self.length
        if self.array[h_value].next == None:
            return -1
        cur = self.array[h_value].next
        while cur != None and cur.key != key:
            cur = cur.next
        
        if cur == None:
            return -1
        return cur.val

        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        h_value = hash(key) % self.length
        cur = self.array[h_value].next
        if self.array[h_value].next == None:
            return -1
        elif cur.key == key:
            cur = cur.next
            self.array[h_value].next = cur
        else:
            while cur.next != None and cur.next.key != key:
                cur = cur.next
            if cur.next != None:
                cur.next = cur.next.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(2,200)
# obj.put(3,300)
# param_2 = obj.get(2)
# print(param_2)
# obj.remove(2)
