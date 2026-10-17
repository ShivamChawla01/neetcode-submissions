class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        nums_dict = defaultdict(list)
        for i in range(len(nums)):
            nums_dict[nums[i]].append(i)
        print(nums_dict)
        for i in nums_dict:
            if(target - i == i and len(nums_dict[i])>1):
                return nums_dict[i][:2]
            elif(target - i != i and target - i in nums_dict):
                return sorted([nums_dict[i][0],nums_dict[target-i][0]])
        return []

        