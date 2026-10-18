class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for i,num in enumerate(nums):
            d[num].append(i)
        i = 0
        j = len(nums)-1
        response = set()
        for i in range(len(nums)-1):
            for j in range(len(nums)-1,i,-1):
                for z in range(i+1,j):
                    if(nums[i]+nums[j]+nums[z] == 0):
                        temp = sorted([nums[i],nums[z],nums[j]])

                        response.add((temp[0],temp[1],temp[2]))
        return list(response)
        


        