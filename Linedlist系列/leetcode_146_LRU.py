class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        dummy_head = Node(1)
        dummy_tail = Node(1)
        self.old = dummy_head
        self.new = dummy_tail
    def get(self, key: int) -> int:
        return 1
    def put(self, key: int, value: int) -> None:
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)