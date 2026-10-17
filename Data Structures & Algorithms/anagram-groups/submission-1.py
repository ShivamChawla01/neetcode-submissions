class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
        alphabet = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        def groupAnagramsHelper(w1):
            arr = [0]*26
            for i in range(len(w1)):
                arr[alphabet[w1[i]]] += 1
            # print(arr)
            d[".".join([str(x) for x in arr])].append(w1)
        for word in strs:
            groupAnagramsHelper(word)
        return list(d.values())




        
            



        