class Solution:

    def encode(self, strs: List[str]) -> str:
        response = ""
        for word in strs:
            response += str(len(word))+'#'+word
        return response

    def decode(self, s: str) -> List[str]:
        response = []
        temp = ""
        for i in range(len(s)):
            if(s[i] == '#'):
                temp = int(temp)
                w = ""
                while(temp):
                    i+=1
                    w += s[i]
                    temp -= 1
                response.append(w)
            elif(s[i] not in ['0','1','2','3','4','5','6','7','8','9']):
                temp = ""
            else:
                temp += s[i]
        return response

