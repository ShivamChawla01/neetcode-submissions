class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        stack = deque([])
        for i in range(len(tokens)):
            if(tokens[i].isalnum()):
                stack.append(int(tokens[i]))
            else:
                if(tokens[i] == '+'):
                    stack.append(stack.pop()+stack.pop())
                elif(tokens[i] == '-'):
                    stack.append(-1*stack.pop()+stack.pop())
                elif(tokens[i] == '*'):
                    stack.append(stack.pop()*stack.pop())
                else:
                    d = stack.pop()
                    n = stack.pop()
                    stack.append(n//d)
        return stack[0]

                    
                    

        