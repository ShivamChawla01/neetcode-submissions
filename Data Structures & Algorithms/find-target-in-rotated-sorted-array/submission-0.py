class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = 0
        while(l<=r):
            mid = (l + r)//2
            if(nums[mid]<nums[mid-1]):
                break
            elif(nums[mid]>nums[-1]):
                l = mid + 1
            else:
                r = mid - 1
        if(target>nums[-1]):
            l = 0
            r = mid
        else:
            l = mid
            r = len(nums) - 1
        while(l<=r):
            mid = (l+r)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] < target):
                l = mid + 1
            else:
                r = mid - 1
        return -1

        