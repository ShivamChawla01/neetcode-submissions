class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = sorted(nums1 + nums2)
        if(len(temp)%2 == 1):
            return temp[(len(nums1)+len(nums2))//2]
        else:
            l = len(temp)//2-1
            r = len(temp)//2
            # print(temp[r-1])
            return temp[l]/2+temp[r]/2
        