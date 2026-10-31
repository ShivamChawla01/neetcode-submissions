class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        response = r
        while(l <= r):
            mid = (l+r)//2
            i = 0
            count = 0
            while(i<len(piles)):
                temp = piles[i]
                count += math.ceil(temp/mid)
                i += 1
            if(count <= h):
                response = min(response,mid)
                r = mid - 1
            else:
                l = mid + 1
        return response
        



        