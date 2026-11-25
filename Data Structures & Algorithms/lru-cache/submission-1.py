class Node:
    def __init__(self,value: int):
        self.val = value
        self.next = None
        self.prev = None
class LRUCache:
    from collections import defaultdict
    def __init__(self, capacity: int):
        self.head = None
        self.end = None
        self.capacity = capacity
        self.lru = defaultdict()

    def get(self, key: int) -> int:
        if(key in self.lru):
            temp = self.lru[key]
            if(temp.prev and temp.next):
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.prev = None
                temp.next = self.head
                self.head = temp
            elif(temp.prev):
                temp.prev.next = None
                temp.prev = None
                temp.next = self.head
                self.head = temp
            return temp.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        print(self.lru)
        if(not self.head):
            self.head = self.end = Node(value)
            self.lru[key] = self.head
            self.capacity -= 1
        else:
            print(self.capacity)
            if(self.capacity>0):
                temp = Node(value)
                temp.next = self.head
                self.head = temp
                self.capacity -= 1
            else:
                print(self.end)
                self.end.val = -1
                self.end = self.end.prev
                if(self.end):
                    self.end.next = None
                temp = Node(value)
                temp.next = self.head
                self.head = temp
            self.lru[key] = temp
        
