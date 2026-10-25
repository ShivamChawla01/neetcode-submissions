class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in range(len(t)):
            d1[t[i]]+=1
        j = 0
        response = ""
        def isValid():
            for i in d1:
                if(d1[i]>d2[i]):
                    return False
            return True
        j = 0
        for i in range(len(s)):
            d2[s[i]] += 1
            while(isValid()):
                if(response == "" or len(response)>i-j+1):
                    response = s[j:i+1]
                d2[s[j]] -= 1
                j+=1
        return response
        