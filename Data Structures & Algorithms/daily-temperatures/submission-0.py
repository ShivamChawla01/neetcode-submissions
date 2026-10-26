class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque
        stack = deque([])
        count = 0
        response = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while(stack and temperatures[stack[-1]] < temperatures[i]):
                temp = stack.pop()
                response[temp] = i-temp
            stack.append(i)
        return response
        