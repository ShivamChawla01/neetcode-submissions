class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        from collections import deque
        stack = deque([])
        combined = []
        # position.sort()
        for i in range(len(position)):
            combined.append((position[i],(target-position[i])/speed[i]))
        combined.sort(key = lambda x:x[0])
        for item in combined:
            if(not stack):
                stack.append(item)
            else:
                temp = stack[-1]
                while(stack and temp[1]<=item[1]):
                    stack.pop()
                    if(stack):
                        temp = stack[-1]
                stack.append(item)
        # print(combined)
        return len(stack)
        
        