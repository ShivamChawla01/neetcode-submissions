class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in range(len(s1)):
            d1[s1[i]]+=1
        j = 0
        for i in range(len(s2)):
            d2[s2[i]] += 1
            while(i-j+1 > len(s1)):
                d2[s2[j]] -= 1
                j += 1
            flag = False
            for item in d1:
                if(d1[item] != d2[item]):
                    flag = True
            if(not flag):
                return True
        return False

        