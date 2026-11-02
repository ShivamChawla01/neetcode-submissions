# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        bottom = head
        front = head
        while(bottom.next):
            bottom = bottom.next
            n-=1
            if(n <= 0):
                front = front.next
        if(front == bottom):
            return None
        temp = front.next
        if(temp):
            front.val = temp.val
            front.next = temp.next
        else:
            return None
        return head
        