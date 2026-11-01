# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = last = head
        while(last and last.next):
            mid = mid.next
            last = last.next
            if(last):
                last = last.next
        prev = None
        temp = mid
        while(mid):
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        temp = head
        l1 = temp
        l2 = prev
        count = 0
        print(prev.val)
        while(temp):
            if(count%2 == 0):
                t = l1
                if(l1):
                    l1 = l1.next
                temp.next = t
                
            else:
                t = l2
                if(l2):
                    l2 = l2.next
                temp.next = t
            temp = temp.next
            count += 1
        


        