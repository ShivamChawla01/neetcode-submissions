class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0):
            return 0
        from collections import defaultdict
        d = defaultdict(int)
        count = 0
        j = 0
        for i in range(len(s)):
            d[s[i]] += 1
            while(d[s[i]]>1):
                d[s[j]] -= 1
                j+=1
            count = max(count,i-j)
            i+=1
        return count+1


        