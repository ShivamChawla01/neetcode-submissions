class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        import bisect
        sorted_list = []
        n = deque([])
        response = []
        j = 0
        for i in range(len(nums)):
            if(len(sorted_list) == k):
                response.append(sorted_list[-1])
            if(len(n) == k):
                temp = n.popleft()
                idx = bisect.bisect_left(sorted_list,temp)
                del sorted_list[idx]
            n.append(nums[i])
            bisect.insort(sorted_list,nums[i])
        # print(n)
        if(sorted_list):
            response.append(sorted_list[-1])
        return response
        