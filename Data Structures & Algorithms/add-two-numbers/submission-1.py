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
            while(head):
                count += 1
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return (prev,count)
        
        temp1 = reverseList(l1)
        temp2 = reverseList(l2)
        if(temp1[1]>=temp2[1]):
            temp2,temp1 = temp1[0],temp2[0]
        else:
            temp2,temp1 = temp2[0],temp1[0]
        temp = temp2
        balance = 0
        while(temp2):
            if(not temp1 and not balance):
                break
            # print(temp1.val , temp2.val , balance)
            if(temp1 and temp2):
                temp2.val = temp1.val + temp2.val + balance
            else:
                if(temp2 and balance):
                    temp2.val = temp2.val + balance
            balance = temp2.val//10
            temp2.val %= 10
            temp2 = temp2.next
            if(temp1):
                temp1 = temp1.next
        t = temp
        if(balance>0):
            temp = ListNode(balance)
            temp.next = t
            # return temp
        response = reverseList(temp)
        # else:
        return response[0]
        
        




        