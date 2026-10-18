class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        fix = 0
        response = []
        while(fix<len(nums)-2):
            if(fix>0 and nums[fix] == nums[fix-1]):
                fix+=1
                continue
            if(nums[fix]>0):
                break
            i = fix+1
            j = len(nums) - 1
            target = -1*nums[fix]
            while(i<j):
                if((nums[i] + nums[j]) == target):
                    response.append([nums[fix], nums[i], nums[j]])
                    i+=1
                    j-=1
                    if(i<j and nums[i] == nums[i-1]):
                        i+=1
                    if(i<j and nums[j] == nums[j+1]):
                        j-=1
                elif((nums[i] + nums[j]) < target):
                    i+=1
                else:
                    j-=1
            fix+=1
        return response


        