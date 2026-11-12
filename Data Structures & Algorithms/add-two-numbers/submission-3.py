# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverseList(head):
            prev = None
            count = 0
            temp = head
            while(temp):
                count += 1
                temp = temp.next
            return(head,count)
        
        temp1 = reverseList(l1)
        temp2 = reverseList(l2)
        if(temp1[1]>=temp2[1]):
            temp2,temp1 = temp1[0],temp2[0]
        else:
            temp2,temp1 = temp2[0],temp1[0]
        temp = temp2
        balance = 0
        while(temp2 and (temp1 or balance>0)):
            
            if(temp1 and temp2):
                temp2.val = temp1.val + temp2.val + balance
            else:
                temp2.val = temp2.val + balance
            balance = temp2.val//10
            temp2.val %= 10
            prev = temp2
            temp2 = temp2.next
            if(temp1):
                temp1 = temp1.next
        if(balance>0):
            prev.next = ListNode(balance)
        # while(temp):
        #     print(temp.val)
        #     temp = temp.next
        return temp

        
        




        