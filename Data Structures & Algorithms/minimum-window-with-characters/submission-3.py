class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in range(len(t)):
            d1[t[i]]+=1
        j = 0
        response = ""
        j = 0
        required = len(d1)
        formed = 0
        for i in range(len(s)):
            d2[s[i]] += 1
            if(s[i] in d1 and d1[s[i]] == d2[s[i]]):
                formed += 1
            while(formed == required):
                if(response == "" or len(response)>i-j+1):
                    response = s[j:i+1]
                if(s[j] in d1 and d1[s[j]] == d2[s[j]]):
                    d2[s[j]] -= 1
                    formed -= 1
                j+=1


        return response
        