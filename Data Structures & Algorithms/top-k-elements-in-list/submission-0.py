class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        tuples = []
        for i in d:
            tuples.append((i,d[i]))
        tuples.sort(key = lambda x: x[1],reverse = True)
        response = []
        i = 0
        while(i < k):
            response.append(tuples[i][0])
            i+=1
        return response
        