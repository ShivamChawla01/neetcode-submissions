class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
        
        def groupAnagramsHelper(w1):
            arr = [0]*26
            for i in range(len(w1)):
                arr[ord(w1[i])-ord('a')] += 1
            # print(arr)
            d[tuple(arr)].append(w1)
        for word in strs:
            groupAnagramsHelper(word)
        return list(d.values())




        
            



        