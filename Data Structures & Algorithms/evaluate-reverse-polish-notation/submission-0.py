class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        stack = deque([])
        for i in range(len(tokens)):
            if(tokens[i] in ['0','1','2','3','4','5','6','7','8','9']):
                stack.append(int(tokens[i]))
            else:
                if(tokens[i] == '+'):
                    stack.append(stack.pop()+stack.pop())
                elif(tokens[i] == '-'):
                    stack.append(-1*stack.pop()+stack.pop())
                elif(tokens[i] == '*'):
                    stack.append(stack.pop()*stack.pop())
                else:
                    stack.append(stack.pop()//stack.pop())
        return stack[0]

                    
                    

        