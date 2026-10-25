class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        from collections import Counter
        d = Counter([])
        
        count = 0
        j = 0
        for i in range(len(s)):
            d[s[i]]+=1
            while(i-j+1-d.most_common()[0][1]>k):
                d[s[j]]-=1
                j += 1
            # print(d,i,j)
            count = max(count,i-j+1)
        return count
                

            
        