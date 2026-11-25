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
        print(self.head.val,self.end.val)
        if(key in self.lru and self.lru[key].val!=-1):
            temp = self.lru[key]
            if(temp.prev and temp.next):
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.prev = None
                temp.next = self.head
                self.head.prev = temp
                self.head = temp
            elif(temp.prev):
                temp.prev.next = None
                self.end = temp.prev
                temp.prev = None
                temp.next = self.head
                self.head.prev = temp
                self.head = temp
            return temp.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        
        if(not self.head):
            self.head = self.end = Node(value)
            self.lru[key] = self.head
            self.capacity -= 1
        else:
            # print(self.capacity)
            print(self.head.val,self.end.val)
            temp = Node(value)
            if(self.capacity>0):
                
                temp.next = self.head
                self.head.prev = temp
                self.head = temp
                self.capacity -= 1
            else:
                self.end.val = -1
                self.end, self.end.prev = self.end.prev, None
                if(self.end):
                    self.end.next = None
                
                temp.next = self.head
                self.head.prev = temp
                self.head = temp
            self.lru[key] = temp
        
