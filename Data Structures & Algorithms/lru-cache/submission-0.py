class ListNode:
    def __init__(self,val,next = None,prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:
    from collections import defaultdict
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = defaultdict()
        self.head = None
        self.end = None
        

    def get(self, key: int) -> int:
        if(key in self.lru):
            temp = self.lru[key]
            if(temp.prev == None):
                return self.lru[key].val
            else:
                temp.prev.next = temp.next
                temp.next = self.head
                self.head = temp
                return temp.val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if(self.head == self.end == None):
            self.head = self.end = ListNode(value)
            self.lru[key] = self.head
            return
        # print(key,value,len(self.lru))
        if(len(self.lru) == self.capacity):
            self.end.val = -1
            self.end = self.end.prev
            if(self.end):
                self.end.next = None
            
        self.lru[key] = ListNode(value)
        temp = self.lru[key]
        temp.next = self.head
        self.head = temp
        
