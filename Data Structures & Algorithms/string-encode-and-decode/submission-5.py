class Solution:

    def encode(self, strs: List[str]) -> str:
        response = ""
        for word in strs:
            response += str(len(word))+'€'+word
        return response

    def decode(self, s: str) -> List[str]:
        response = []
        temp = ""
        for i in range(len(s)):
            if(s[i] == '€'):
                t = int(temp)
                w = ""
                while(t):
                    i+=1
                    if(i>=len(s)):
                        break
                    w += s[i]
                    t -= 1
                response.append(w)
            elif(s[i] not in ['0','1','2','3','4','5','6','7','8','9']):
                temp = ""
            else:
                temp += s[i]
        return response

