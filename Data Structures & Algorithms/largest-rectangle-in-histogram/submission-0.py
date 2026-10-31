class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        from collections import deque
        stack = deque([])
        left = []
        right = [-1]*len(heights)
        for i in range(len(heights)):
            if(not stack):
                stack.append((i,heights[i]))
                left.append(-1)
            else:
                temp = stack[-1]
                while(stack and temp[1] >= heights[i]):
                    stack.pop()
                    if(stack):
                        temp = stack[-1]
                    else:
                        temp = (-1,-1)
                left.append(temp[0])
                stack.append((i,heights[i]))
        stack = deque([])
        for i in range(len(heights)-1,-1,-1):
            if(not stack):
                stack.append((i,heights[i]))
                right[i] = len(heights)
            else:
                temp = stack[-1]
                while(stack and temp[1] >= heights[i]):
                    stack.pop()
                    if(stack):
                        temp = stack[-1]
                    else:
                        temp = (len(heights),-1)
                right[i] = temp[0]
                stack.append((i,heights[i]))
        maximum = 0
        for i in range(len(left)):
            if(left[i] == -1):
                l = heights[0]
            else:
                l = heights[left[i]]
            if(right[i] == len(heights)):
                r = heights[-1]
            else:
                r = heights[right[i]]
            maximum = max(maximum, (right[i]-left[i]-1)*heights[i])
        # print(left)
        # print(right)
        return maximum
        
        




        