class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = nums + []
        right = [1]*len(nums)
        right = nums + []
        for i in range(1,len(nums)):
            left[i]*=left[i-1]
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i]*right[i+1]
        response = [1]*len(nums)
        for i in range(1,len(nums)-1):
            response[i] = left[i-1]*right[i+1]
        response[0] = right[1]
        response[len(nums)-1] = left[len(nums)-2]
        return response
        
        