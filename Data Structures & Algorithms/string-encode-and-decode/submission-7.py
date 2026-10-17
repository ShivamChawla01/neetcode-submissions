class Solution:

    def encode(self, strs: List[str]) -> str:
        response = ""
        for word in strs:
            response += str(len(word))+'#'+word
        return response

    def decode(self, s: str) -> List[str]:
        response = []
        i = 0
        while(i < len(s)):
            j = s.index('#',i)
            length = int(s[i:j])
            i = j+1
            response.append(s[i:i+length])
            i = i+length
        return response

