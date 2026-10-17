class Solution:

    def encode(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return "-1"
        return ".".join(strs)

    def decode(self, s: str) -> List[str]:
        print(s.strip())
        if(s == "-1"):
            return []
        if(len(s.strip()) == 0):
            return [""]
        
        return s.split('.')
