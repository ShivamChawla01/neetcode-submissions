class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack = deque([])
        for i in range(len(s)):
            if(s[i] in ['(','{','[']):
                stack.append(s[i])
            else:
                if(not stack):
                    return False
                temp = stack.pop()
                if(s[i] == ')' and temp != '('):
                    return False
                elif(s[i] == '}' and temp != '{'):
                    return False
                elif(s[i] == ']' and temp != '['):
                    return False
        return len(stack) == 0
                
        