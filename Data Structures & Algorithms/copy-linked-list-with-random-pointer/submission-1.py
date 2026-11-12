"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(not head):
            return None
        prev = None
        start = head
        while(head):
            temp = head.next
            head.next = Node(head.val)
            head = head.next
            head.next = temp
            head = temp
        
        head = start
        while(head):
            temp = head.next
            if(head.random):
                temp.random = head.random.next
            head = head.next.next
        head = start.next
        while(head.next):
            head.next = head.next.next
            head = head.next
        return start.next
        

            
        