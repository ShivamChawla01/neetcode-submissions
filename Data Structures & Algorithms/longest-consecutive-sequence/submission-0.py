class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        count = 0
        maxCount = 0
        for i in range(len(nums)):
            if(nums[i]-1 not in visited):
                num = nums[i]
                while(num in visited):
                    count+=1
                    num+=1
                maxCount = max(maxCount, count)
                count = 0
        return maxCount

                
        
        