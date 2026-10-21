from collections import deque
class Solution:
    
    def trap(self, height: List[int]) -> int:
        total = 0
        stack = deque([])
        i = 0
        while(i<len(height)):
            while(stack and height[i]>height[stack[-1]]):
                bottom = stack.pop()
                if(not stack):
                    break
                left = stack[-1]
                total += (min(height[left],height[i]) - height[bottom])*(i-left-1)
            stack.append(i)
            i+=1
        return total
        