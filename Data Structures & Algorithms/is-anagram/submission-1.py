class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        from collections import defaultdict
        occurence = defaultdict(int)
        for i in range(len(s)):
            occurence[s[i]] += 1
        for i in range(len(t)):
            occurence[t[i]] -= 1
            if(occurence[t[i]] < 0):
                return False
        return True

        