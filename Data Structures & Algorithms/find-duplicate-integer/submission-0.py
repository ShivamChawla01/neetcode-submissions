class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        flag = False
        while(fast>-1):
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if(slow == fast):
                break
        slow = 0
        while(slow != fast):
            slow = nums[slow]
            fast = nums[fast]
        return fast

        