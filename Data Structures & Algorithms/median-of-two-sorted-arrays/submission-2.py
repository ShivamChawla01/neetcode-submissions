class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        smaller = nums1 if(len(nums1)<len(nums2)) else nums2
        larger = nums2 if(len(nums2)>len(nums1)) else nums1
        l1 = 0
        r1 = len(smaller)
        half = (len(nums1) + len(nums2) + 1)//2
        while(l1<=r1):
            mid = (l1+r1)//2
            j = half-mid
            # a,b,c,d = larger[mid-1],larger[mid+1],smaller[j-1],smaller[j+1]
            s_left  = smaller[mid-1] if mid > 0 else float('-inf')
            s_right = smaller[mid]   if mid < len(smaller) else float('inf')
            l_left  = larger[j-1]    if j > 0   else float('-inf')
            l_right = larger[j]      if j < len(larger)   else float('inf')
            if(s_left > l_right):
                r1 = mid - 1
            elif(l_left > s_right):
                l1 = mid + 1
            else:
                if((len(smaller) + len(larger))%2 == 1):
                    return max(s_left,l_left)
                else:
                    return (max(s_left,l_left) + min(s_right,l_right))/2.0
        return 0


            

            

        