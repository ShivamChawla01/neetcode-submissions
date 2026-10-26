class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        stack = deque([])
        for i in range(len(tokens)):
            # print(stack,tokens[i])
            if(tokens[i].lstrip('-').isalnum()):
                # print(tokens[i])
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
                    stack.append(int(n/d))
        return stack[0]

                    
                    

        