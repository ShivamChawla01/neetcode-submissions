class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        nums_dict = defaultdict(list)
        for i in range(len(nums)):
            complement = target - nums[i]
            if(complement in nums_dict):
                return [nums_dict[complement],i]
            nums_dict[nums[i]] = i
        return []


        