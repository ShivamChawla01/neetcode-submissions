class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter([])
        j = 0
        response = []
        for i in range(len(nums)):
            if(i-j+1 == k):
                response.append(max(nums[j:i+1]))
                j+=1
        return response
        